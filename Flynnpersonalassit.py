import spotipy
import wikipedia
import os
import pywhatkit
import datetime
import pyjokes
import speech_recognition as sr
import pyttsx3

hearme = sr.Recognizer()
ttsx = pyttsx3.init()


def talk(text):
    ttsx.say(text)
    ttsx.runAndWait()

# ttsx.say('Babe i can listen to you')


# talk('Bro i can listen to you')


def wishMe():
    print('WELCOME')
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk("Good Morning !")

    elif hour >= 12 and hour < 18:
        talk("Good Afternoon ! ")

    else:
        talk("Good Evening ! ")

    assname = ("Flynn")
    talk("My name is " + assname + ' I am here to help you')
    # talk('You should have programmed me with a better quote')


def takename():
    talk("What should i call you?")
    name = convo()
    talk("okay...." + name)

    talk("what can i do for you ? ")


def convo():
    try:
        with sr.Microphone() as src:

            voice = hearme.listen(src)
            order = hearme.recognize_google(voice)

    except:
        pass
    return order


def run_babe():

    order = convo()

    if 'play' in order:
        hehe = order.replace('play', '')
        talk('oh my gawd! you love' + hehe + 'Dont you? Playing ' + hehe)
        # print('swag face swag face')
        pywhatkit.playonyt(hehe)
    elif 'time' in order:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The time is ' + time)
    elif 'tell me about' in order:
        wiki = order.replace('tell me about', '')
        info = wikipedia.summary(wiki, 1)
        print(info)
        talk(info)
    elif 'movie' in order:
        talk(' hahaha very funny lol Never!! First complete your work bitch?')
    elif 'joke' in order:
        talk('apart from your life? Yeah sure ')
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
        talk('ha ha ha ha ha ha ha')
    elif 'talk back' in order:
        talk('why?? i got a mouth of my own, I dont use yours ')
    # elif 'play music' in order or "play song" in order:
    #     songs = os.listdir("C:\\Users\\Nandini_Jaryal\\Music")
    #     print(songs)
    elif 'stop' in order:
        talk('stoping.....in... 1....... 2....... 3.......')
        exit()

    else:
        talk('Did you say something? I did not get it TRY AGAIN ')


wishMe()
takename()
while True:
    run_babe()
