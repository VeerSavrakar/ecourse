from django import forms


class FormNmae(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    text=forms.CharField(widget=forms.Textarea)