import speech_recognition as sr

def listen() :
    r = sr.Recognizer()
    with sr.Microphone() as source:

        audio = r.listen(source)
    text = r.recognize_google(audio)
    return text