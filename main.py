import torch
import streamlit as st
from generator import generate_audio


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


if __name__ == "__main__":
    main()
