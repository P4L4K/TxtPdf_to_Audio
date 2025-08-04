import streamlit as st
from gtts import gTTS
import PyPDF2 as pdf
from gtts.lang import tts_langs

st.write('File to Audio')

@st.cache_resource


    
def fetch_pdf_text(file):
    reader=pdf.PdfReader(file)
    text=""
    for page in reader.pages:
        content=page.extract_text()
        if content:
            text +=content
    return text
    
def create_audio(text,language):
    file_text=gTTS(text,lang=language)
    file_text.save('file_audio.mp3')
    st.success('Audio file created successfully!')

def download_audio():
    with open('file_audio.mp3', 'rb') as audio_file:
        audio = audio_file.read()
    st.download_button(label='Download Audio', data=audio, file_name='file_audio.mp3', mime='audio/mp3')

def play_audio():
    with open('file_audio.mp3','rb') as audio_file:
        audio=audio_file.read()
    st.audio(data=audio,format='audio/mp3')
                    

upload_f = st.file_uploader('Choose a file', type = ['txt','pdf'])

available_language_name=list(tts_langs().values())
available_language_code=list(tts_langs().keys())
language_name= st.selectbox('Select Language',available_language_name, index=available_language_code.index('hi'))
language_code = available_language_code[available_language_name.index(language_name)]


if upload_f:
    if st.button('Create Audio', type='primary'):
        if upload_f.type=='text/plain':
            create_audio(upload_f.read().decode('utf-8'),language_code)
        else:
            create_audio(fetch_pdf_text(upload_f),language_code)
        download_audio()
        play_audio()
