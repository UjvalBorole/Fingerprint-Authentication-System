from django.shortcuts import render, HttpResponse
import os
import cv2

# Create your views here.


def viewdata(loc):
    try:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        MEDIA_ROOT = os.path.join(BASE_DIR, 'finger/')

        # loc = "1__M_Left_index_finger_CR.BMP"
        data = (str(MEDIA_ROOT)+"fingerimg/altered/" + str(loc))

        sample = cv2.imread(data)
        # sam = cv2.resize(sample, None, fx=2.5, fy=2.5)

        # cv2.imshow("sample_image", sample)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        best_score = 0
        filename = None
        image = None
        kp1, kp2, mp = None, None, None

        for file in [file for file in os.listdir(str(MEDIA_ROOT) + "/fingerimg/real")]:
            fingerprint_image = cv2.imread(
                str(MEDIA_ROOT) + "/fingerimg/real/" + file)

            sift = cv2.SIFT_create()

            image8bit = cv2.normalize(
                fingerprint_image, None, 0, 255, cv2.NORM_MINMAX).astype('uint8')

            keypoints_1, descriptors_1 = sift.detectAndCompute(sample, None)
            keypoints_2, descriptors_2 = sift.detectAndCompute(
                image8bit, None)

            matches = cv2.FlannBasedMatcher(dict(algorithm=1, trees=10), dict()).knnMatch(
                descriptors_1, descriptors_2, k=2)
            match_points = []

            for p, q in matches:
                if p.distance < 0.1*q.distance:
                    match_points.append(p)

            keypoint = 0
            if len(keypoints_1) < len(keypoints_2):
                keypoint = len(keypoints_1)

            else:
                keypoint = len(keypoints_2)

            if len(match_points) / keypoint * 100 > best_score:
                best_score = len(match_points) / keypoint * 100
                filename = file
                image = fingerprint_image
                kp1, kp2, mp = keypoints_1, keypoints_2, match_points
                result = cv2.drawMatches(
                    sample, kp1, fingerprint_image, kp2, mp, None)

        path = 'C:/personal/fingerprint authentication/authentication/finger/static/img_result'
        cv2.imwrite(os.path.join(path, 'result_image.jpg'), result)
        print("Best Match:" + filename)
        print("Score:" + str(best_score))

        return best_score
    except:
        return "Something wents Wrong"

# viewdata()


def index(request):
    if request.method == "POST":

        my_uploaded_file = request.FILES['my_uploaded_file']
        data = str(my_uploaded_file)
        # print(type(data))
        print(data)
        cd = viewdata(data)

        return render(request, 'smg.html', {'data': cd})

    else:
        return render(request, 'smg.html')
