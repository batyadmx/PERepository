from TTS.api import TTS


def generate_audio(text, path):
    device = "cuda" if torch.cuda.is_available() else "cpu"

    tts = TTS(model_name="tts_models/en/ljspeech/speedy-speech", progress_bar=False).to(device)
    tts.tts_to_file(text=text, file_path=path)

    with open(path, "rb") as file:
        file_content = file.read()

    return file_content
