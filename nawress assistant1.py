import speech_recognition as sr
import pyttsx3 as py
import pywhatkit
import datetime
import time



listen = sr.Recognizer()
assistant = py.init()
assistantvoice = assistant.getProperty("rate")
assistant.setProperty("rate", 180)
voice = assistant.getProperty("voices")
assistant.setProperty("voices", voice[1])

def parler(text):
    assistant.say(text)
    assistant.runAndWait()

def salut():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        parler("bonjour noussa")
    elif hour >= 12 and hour < 19:
        parler("salut noussa")
    else :
        parler("bonsoir noussa")

def command():
    speech = sr.Recognizer()
    with sr.Microphone() as source:
        speech.energy_threshold = 10000
        speech.adjust_for_ambient_noise(source, 1.2)
        print("bonjour noussa, je suis en train d'ecouter")

        while True:
            reponse = speech.listen(source)
            try:
                text = speech.recognize_google(reponse, language='fr_FR')
                print(text)
                if "bonjour" in text:
                    parler("bonjour")
                elif "ça va" in text:
                    parler("oui tres bien")
                elif "oui" in text:
                    parler("c'es bien")
                elif "quelle heure est-il maintenant" in text:
                    heure = datetime.datetime.now().strftime("%H:%M")
                    parler("il est" + heure)
                elif "je veux écouter la chanson de" in text:
                    chanson = text.replace('je veux écouter la chanson de', '')
                    print(chanson)
                    parler("d'accord noussa")
                    pywhatkit.playonyt(chanson)
                else :
                    parler("je ne comprend pas")

            except Exception as ex:
                parler("je n'ecoute rien")

def main():
    salut()
    command()


if __name__ == "__main__":
    main()





