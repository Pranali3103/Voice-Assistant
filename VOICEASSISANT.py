import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Shanaya' in command:
                command = command.replace('Shanaya', '')
                print(command)
            return command  # This line was missing in the original code
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
    except sr.RequestError:
        print("Sorry, there was an error with the request to the speech recognition service.")
    return ''


def shanaya():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + current_time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        try:
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
            talk(f"There are multiple results for {person}. Please be more specific.")
        except wikipedia.exceptions.PageError:
            print(f"No information found for {person}.")
            talk(f"I couldn't find any information about {person}.")
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    shanaya()
