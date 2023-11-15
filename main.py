import torch
from TTS.api import TTS

device = "cuda" if torch.cuda.is_available() else "cpu"
tts = TTS(model_name="tts_models/en/ljspeech/speedy-speech", progress_bar=False).to(device)
tts.tts_to_file(text="MAXIM AND SANYA.", file_path="output.wav")