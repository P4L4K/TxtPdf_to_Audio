import streamlit as st
from gtts import gTTS
import PyPDF2 as pdf


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
    
def create_audio(text):
    file_text=gTTS(text)
    file_text.save('file_audio.mp3')

def download_audio():
    with open('file_audio.mp3', 'rb') as audio_file:
        audio = audio_file.read()
    st.download_button(label='Download Audio', data=audio, file_name='file_audio.mp3', mime='audio/mp3')

upload_f = st.file_uploader('Choose a file', type = ['txt','pdf'])
if upload_f:
    if upload_f.type=='text/plain':
        create_audio(upload_f.read().decode('utf-8'))
    else:
        create_audio(fetch_pdf_text(upload_f))

    download_audio()
    st.success('Audio file created successfully!')
