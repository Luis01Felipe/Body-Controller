import speech_recognition as sr


def reconhecer_comando():
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Diga o comando:")
        audio = recognizer.listen(mic)
    try:
        comando = recognizer.recognize_google(audio, language="pt-BR")
        return comando.lower()
    except sr.UnknownValueError:
        return "Comando não entendido"
