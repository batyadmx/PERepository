from TTS.api import TTS
import torch


def generate_audio(text, path):
    if not validate_input_text(text):
        raise Exception("Bad string. String must be >20 <100 idiot")

    device = "cuda" if torch.cuda.is_available() else "cpu"

    tts = TTS(model_name="tts_models/en/ljspeech/speedy-speech", progress_bar=False).to(device)
    tts.tts_to_file(text=text, file_path=path)

    with open(path, "rb") as file:
        file_content = file.read()

    return file_content


def validate_input_text(text):
    return 20 < len(text) < 100
