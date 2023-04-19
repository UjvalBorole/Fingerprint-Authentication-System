from django.contrib import admin
from django.urls import path
from finger import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    # path('main/', views.mainfile, name='main'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
