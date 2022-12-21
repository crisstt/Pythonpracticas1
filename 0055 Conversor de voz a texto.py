import speech_recognition as sr

#crear recognicimiento
r = sr.Recognizer()

#           permite el uso del microfono que este predeterminado
with sr.Microphone() as source:
    print('Puede Hablar...')
    audio = r.listen(source)

    try:
        texto = r.recognize_google(audio, language = 'es - Es')
        print('La transcripción es : {}'. format(texto))
    except:
        print('¡Lo Siento! ¡No Pude Entender!')
