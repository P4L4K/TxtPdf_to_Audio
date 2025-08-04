# PdfTxt_to_Audio

This project converts PDF and text files into audio files using text-to-speech technology. It is designed to help users listen to the content of their documents, making information more accessible and convenient.

## Features
- Convert PDF files to audio (mp3)
- Convert plain text files to audio
- Supports multiple languages
- Allows the users to download the audio

## Requirements
- Python 3.7+
- Required Python packages (install with pip):
  - PyPDF2
  - gTTS 
  - streamlit

## Installation
1. Clone this repository or download the source code.
2. Install the required packages:
   ```powershell
   pip install PyPDF2 gTTS streamlit
   ```

## Usage

To launch the web interface, run:

```powershell
streamlit run app.py
```

This will open a browser window where you can upload PDF or text files and download the generated audio.

## License
This project is licensed under the MIT License.

## Acknowledgements
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [gTTS](https://pypi.org/project/gTTS/)

