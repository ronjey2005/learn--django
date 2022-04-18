from django.shortcuts import render
from googletrans import LANGUAGES
from .translator import translate_input

# Create your views here.
def TranslatorView(request):
    if request.method == 'POST':
        original_text = request.POST['my_textarea']
        dest_lang = request.POST['languages']
        print(dest_lang)
        translated_text = translate_input(original_text, dest_lang)
        context = {
            "original_text": original_text,
            "translated_text": translated_text,
            "lang_codes": LANGUAGES,
            "selected_lang": dest_lang
        }
        return render(request,'templates/translator/translator.html', context)
    else:
        context = {
            "original_text": "",
            "translated_text": "",
            "lang_codes": LANGUAGES
        }
        return render(request, 'templates/translator/translator.html', context)



