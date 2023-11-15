import speech_recognition as sr
import pyttsx3 as tts


r = sr.Recognizer()
engine = tts.init()
engine.setProperty('rate', 125)
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PL-PL_PAULINA_11.0')

def mow(text):
    engine.say(text)
    engine.runAndWait()

def getText():
    with sr.Microphone() as source:
        try:
            print("Słucham...")
            audio = r.listen(source)
            text = r.recognize_google(audio, language='pl-PL')
            if text != "":
                return text
            return 0
        except:
            return 0

while True:
    txt = getText()
    if not txt == 0:
        print(txt)
        mow(txt)
        break
    else:
        print("Nie udało się rozpoznać...")
        continue

# for voice in engine.getProperty('voices'):
#     print(voice)