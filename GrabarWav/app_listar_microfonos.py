import sounddevice as sd

# Imprime la lista de dispositivos de entrada de micrófono
audio_devices = sd.query_devices()
input_microphone_devices = [device for device in audio_devices if 'input' in device['name'].lower()]
print("Dispositivos de entrada de micrófono disponibles:")
for idx, device in enumerate(input_microphone_devices):
    print(f"{idx + 1}: {device['name']} (ID: {device['name']})")