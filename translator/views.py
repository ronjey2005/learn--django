from django.shortcuts import render
#from .models import Post
from django.views import generic

# Create your views here.
class TranslatorView(generic.TemplateView):
    template_name = 'templates/translator.html'
    context_object_name = "translator_view"



