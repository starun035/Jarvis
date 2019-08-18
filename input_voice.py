import speech_recognition as sr


# receives an audio inside the function and returns text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:               # source = sr.Microphone, handles exceptions as well
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            print(e)
            print("Say that again Please...")
            return "Nothing"
        return query
