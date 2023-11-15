import speech_recognition as sr
import elevenlabs
import creds


r = sr.Recognizer()
elevenlabs.set_api_key(creds.api_key)
voiceAI = elevenlabs.Voice(
    voice_id = "2EiwWnXFnvU5JabPnv8n",
)

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
        audioAI = elevenlabs.generate(text=txt, voice=voiceAI)
        elevenlabs.play(audioAI)
        break
    else:
        print("Nie udało się rozpoznać...")
        continue
