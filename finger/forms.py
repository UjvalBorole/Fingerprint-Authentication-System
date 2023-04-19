from django import forms


class Fingerprint(forms.Form):
    file = forms.FileField()
