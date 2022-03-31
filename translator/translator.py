from googletrans import Translator

def translate_input(user_text, dest_lang):
    translator = Translator()
    translated_output = translator(text=user_text,dest=dest_lang).text
    print(translated_output)
    return translated_output