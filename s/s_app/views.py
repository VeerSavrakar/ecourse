# from django.shortcuts import render
# from s_app import forms
# from django.views.generic import CreateView
# from django.urls import reverse_lazy

from django.views.generic import CreateView
from django.urls import reverse_lazy
from . import forms

class CreateForm(CreateView):
    form_class = forms.Form
    success_url = reverse_lazy('logi')
    template_name = 's_app/signup.html'

