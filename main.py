import whisper

model = whisper.load_model("medium")
result = model.transcribe("C:/Users/ihlop/PycharmProjects/whisper/audio_2023-11-19_20-14-08.ogg")
print(result["text"])