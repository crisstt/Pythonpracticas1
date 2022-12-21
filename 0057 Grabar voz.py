import sounddevice as sd
from scipy.io.wavfile import write
import time

# standard sample rate: 44.1 KHZ (Or 48.0 KHZ)
fs = 44100
# fs = 48000

# grabar segundos

sec = 20

print('Iniciando el Programa de Grabacion.... Porfavor Espere!')
waiting = time.sleep(1.5)

voice_record = sd.rec(int(sec * fs), samplerate = fs, channels = 2)

sd.wait()

# esperando the archivo WAV
write('prueba.wav', fs, voice_record)

