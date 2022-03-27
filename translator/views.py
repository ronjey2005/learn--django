from django.shortcuts import render

# Create your views here.
def TranslatorView(request):
    if request.method == 'POST':
        original_text = request.POST['my_textarea']
        translated_text = original_text.upper()
        context = {"original_text": original_text, "translated_text": translated_text}
        return render(request,'templates/translator.html', context)
    else:
        #original_text = request.POST['my_textarea']
        context = {"original_text": "", "translated_text": ""}
        return render(request, 'templates/translator.html', context)



