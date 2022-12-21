import speech_recognition as sr
import time

#crear recognicimiento
r = sr.Recognizer()

#           permite el uso del microfono que este predeterminado
with sr.AudioFile('C:\\Users\\zxxma\\Documents\\Grabaciones de sonido\\Grabación.wav') as source:
    audio = r.listen(source)

    try:
        print('Leyendo Audio Del Archivo, Porfavor, Espere un Momento.....')
        texto = r.recognize_google(audio, language = 'es - Es')
        time.sleep(1.5)
        print(texto)
    except:
        print('¡Lo Siento! ¡No Pude Entender!')
