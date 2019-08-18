import smtplib
import Speak, input_voice

# Accessing user's confidential information
file = open("mail_info.txt", 'r')
mail_id, mail_pass = file.read().split(' ')
file.close()


def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(mail_id, mail_pass)
    server.sendmail('starun035@gmail.com', to, content)
    server.close()

# List of all names with their corresponding mail addresses
mail_add = {'tarun': 'starun034@yahoo.com', 'naveen': 'snaveen069@gmail.com', 'vandit': 'jainvandit25@gmail.com'}


def mail_to_person(query):
    flag = 0
    for key in mail_add:
        if key in query:
            query = key
            flag = 1
            break
    if flag == 0:
        print("Sorry, The mail address for this name does not exist in database")
        Speak.speak("Sorry, The mail address for this name does not exist in database")
        return

    try:
        Speak.speak("What should i say?")
        content = input_voice.takecommand()
        to = mail_add[query]
        sendmail(to, content)
        print('Email has been sent')
        Speak.speak('Email has been sent')
    except Exception as e:
        print(e)
        echo = "Sorry sir, I was not able to send you email, please try again"
        print(echo)
        Speak.speak(echo)
