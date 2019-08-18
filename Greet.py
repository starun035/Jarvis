import datetime
import Speak

# greets the user
def wishme():

    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        Speak.speak("Good Morning Sir")
    elif 12 <= hour < 17:
        Speak.speak("Good Afternoon Sir")
    else:
        Speak.speak("Good Evening Sir")
    Speak.speak('I\'m Naiinaa, speed 1 Tera Hertz, memory 1 ZetaByte')