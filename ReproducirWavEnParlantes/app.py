

##------ 

# leyendo un fichero wav

import soundfile as sf

entrada="salida.wav"

audio, sampling_rate = sf.read("salida.wav")

##------ 
# reproduciendo un fichero wav

import sounddevice as sd

sd.play(audio, sampling_rate)
sd.wait()