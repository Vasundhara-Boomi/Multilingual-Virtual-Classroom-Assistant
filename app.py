import os
import pygame
from gtts import gTTS
import streamlit as st
import speech_recognition as sr
from googletrans import LANGUAGES, Translator
import translate_text
import comprehension_check
import translate_voice

translator = Translator()

def main(): 
    pygame.mixer.quit()  # Initialize the mixer module.
    st.set_page_config(page_title='Multilingual Virtual Classroom Assistant', page_icon='📚')   # Set page title and icon
    page = st.sidebar.radio('Explore', [ 'Comprehension Check', 'Text Language Translator'])

    if page == 'Comprehension Check':
        comprehension_check.page_1()

    elif page == 'Text Language Translator':
        translate_text.page_2()

# Create a mapping between language names and language codes
language_mapping = {name: code for code, name in LANGUAGES.items()}

def get_language_code(language_name):
    return language_mapping.get(language_name, language_name)

def translator_function(spoken_text, from_language, to_language):
    return translator.translate(spoken_text, src='{}'.format(from_language), dest='{}'.format(to_language))

def text_to_voice(text_data, to_language):
    myobj = gTTS(text=text_data, lang='{}'.format(to_language), slow=False)
    # myobj.save("cache_file.mp3")
    # audio = pygame.mixer.Sound("cache_file.mp3")  # Load a sound.
    # audio.play()
    # os.remove("cache_file.mp3")

if __name__ == "__main__":
    main()
