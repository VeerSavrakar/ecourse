from django.shortcuts import render
from django.forms import Form
from django.views.generic import CreateView,TemplateView
from django.urls import reverse_lazy

class indexform(TemplateView):
    template_name='index.html'
class thanks(TemplateView):
    template_name='thanks.html'
    
class test(TemplateView):
    template_name='test.html'