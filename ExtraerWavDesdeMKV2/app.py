import moviepy.editor as mp

# Nombre del archivo MKV de entrada
input_file = "creando_hilos.mkv"

# Nombre del archivo WAV de salida
output_file = "salida.wav"

# Cargar el archivo MKV
clip = mp.VideoFileClip(input_file)

# Extraer el audio del clip de video
audio = clip.audio

# Guardar el audio como archivo WAV con la frecuencia de muestreo deseada (16 kHz)
audio.write_audiofile(output_file, codec="pcm_s16le", fps=16000)

print("Audio extraído y guardado en", output_file)
