import PyPDF2
import requests
import os
from gtts import gTTS

def pdf_to_text(pdf_path):
    """Extract text from a PDF file."""
    text = ""
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text() + "\n"
    return text

def text_to_speech(text, output_file="output_audio.mp3"):
    """Convert text to speech using Google Text-to-Speech."""
    tts = gTTS(text=text, lang="en")
    tts.save(output_file)
    print(f"Audio saved as {output_file}")

# Provide the path to your PDF file
pdf_path = "C:\Users\USER\Desktop\pinky\Prescription_2409010001Y_1.pdf"
text = pdf_to_text(pdf_path)

# Convert extracted text to speech and save as an audio file
if text:
    text_to_speech(text)
else:
    print("No text extracted from PDF.")
