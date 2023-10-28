import sounddevice as sd
import wave

duration = 10  # Duración de la grabación en segundos
samplerate = 16000  # Frecuencia de muestreo (ejemplo: 16000 Hz)

print("Iniciando grabación...")
audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype="int16")
sd.wait()
print("Grabación finalizada")

filename = "salida.wav"  # Nombre del archivo de audio de salida
print("Audio grabado. Guardando en", filename)
with wave.open(filename, 'wb') as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(samplerate)
    wf.writeframes(audio.tobytes())