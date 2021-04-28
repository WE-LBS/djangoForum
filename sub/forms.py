from django import forms

class CreatePost(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(max_length=400)
    author = forms.CharField(max_length=40)