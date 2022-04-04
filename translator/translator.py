from googletrans import Translator

def translate_input(user_text, dest_lang):
    translator = Translator()
    print(translator)
    print(user_text + ' \n ' + dest_lang)
    translated_output = translator.translate(user_text, dest=dest_lang).text
    return translated_output