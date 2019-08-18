import datetime
import wikipedia
import os
import random
import Speak, Send_mail, Web_crawl, Open_url


def process_query(query):
    if 'about' in query:
        query = query.replace('about', '')
        result = wikipedia.summary(query, sentences=1)
        print(result)
        Speak.speak('According to wikipedia' + result)
        return

    elif 'music' in query:
        music_dir = 'F:\\Muzic\\90\'s superhit'
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, random.choice(songs)))
        return

    elif 'time' in query:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        print('Time is:' + time)
        Speak.speak(time)
        return

    elif 'notepad' in query:
        notepad_path = "C:\\Users\\Naveen Sharma\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad"
        os.startfile(os.path.join(notepad_path))
        return

    elif 'mail' in query:
        Send_mail.mail_to_person(query)
        return

    elif 'camera' in query:
        pass

    elif 'open' in query:
        query = query.replace('open ', '')
        print(f'Opening {query}...\n')
        Web_crawl.get_url('https://www.google.com/search?q=' + query)
        return
    else:
        print(f'Showing web results for: {query}')
        Open_url.open('https://www.google.com/search?q=' + query)
