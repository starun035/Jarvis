import Greet, Speak, input_voice
import Process_query

if __name__ == "__main__":

    Greet.wishme()
    Speak.speak('How may I help you')
    while True:
        query = input_voice.takecommand().lower()
        if 'quit' in query:
            Speak.speak('Thanks for your valuable time Sir. It was great to help you!')
            break
        Process_query.process_query(query)

