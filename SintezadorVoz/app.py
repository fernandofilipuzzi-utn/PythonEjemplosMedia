from gtts import gTTS
from playsound import playsound


input ="hola, ¡soy la bomba! ... ¡tucumana!, ja ja ja!"

tts = gTTS(text=input, lang='es')

tts.save('salida.mp3')
playsound('salida.mp3')