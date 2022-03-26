from django.shortcuts import render

# Create your views here.
def TranslatorView(request):
    context = {"translator_view" : "translator_view"}
    return render(request,'templates/translator.html', context)



