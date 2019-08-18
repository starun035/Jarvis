# from win32com.client import Dispatch
#
# # takes text as input and audio as output
# def speak(audio):
#     speak = Dispatch("SAPI.SpVoice")
#     speak.Speak(audio)

import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
# print(voices[0].id)
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):

    engine.say(audio)
    engine.runAndWait()
