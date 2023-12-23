import torch
import streamlit as st
from TTS.api import TTS

def main():
    st.title("TEXT TO SPEECH")

    text_input = st.text_area("Введите ваш текст здесь. Текст должен быть на английском!", height=200)
    
    if st.button("Перевести в аудио"):
        download_text_file(text_input)

def download_text_file(text_content):
    audio_file = "output.wav"

    st.download_button(
        label="Скачать файл",
        key="text_download_button",
        file_name=audio_file,
        data=generate_audio(text_content, audio_file)
    )

def generate_audio(text, path):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    tts = TTS(model_name="tts_models/en/ljspeech/speedy-speech", progress_bar=False).to(device)
    tts.tts_to_file(text=text, file_path=path)

    with open(path, "rb") as file:
        file_content = file.read()

    return file_content


if __name__ == "__main__":
    main()