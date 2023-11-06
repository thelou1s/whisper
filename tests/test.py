import whisper

model = whisper.load_model("base")
result = model.transcribe("15s.wav")
print(result["text"])