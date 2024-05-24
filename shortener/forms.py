from django import forms

class ShortenForm(forms.Form):
    url = forms.URLField(label="URL to shorten", required=True)