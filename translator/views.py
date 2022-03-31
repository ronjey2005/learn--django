from django.shortcuts import render
from .translator import translate_input

# Create your views here.
def TranslatorView(request):
    if request.method == 'POST':
        original_text = request.POST['my_textarea']
        #translated_text = original_text.upper()
        translated_text = translate_input(original_text,'de')
        print(translated_text)
        context = {"original_text": original_text, "translated_text": translated_text}
        return render(request,'templates/translator.html', context)
    else:
        #original_text = request.POST['my_textarea']
        context = {"original_text": "", "translated_text": ""}
        return render(request, 'templates/translator.html', context)



