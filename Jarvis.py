import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import wolframalpha
import pywhatkit
import pyjokes
import chatbot


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M %p")
    speak(Time)
    print("Jarvis:Sir,the time is",Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak(day)
    speak(month)
    speak(year)
    print("Jarvis: Sir,today is",day, month, year)


def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=8, phrase_time_limit=4)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
            # print(e)
        print("Say that again please.....")
        return "None"
    return query

def unlock():
    while True:
        speak("Please tell the Password")
        print("Jarvis: Please tell the Password")
        User_Id = takeCommand()
        password = "activate Jarvis"
        if password == User_Id:
            speak("Access Granted")
            print("Jarvis: Access Granted")
            break
        else:
            speak("Access Denied")
            print("Jarvis: Access Denied")


def wishMe():

    hour = int(datetime.datetime.now().hour)
    tt = datetime.datetime.now().strftime("%I:%M %p")
    if hour>= 0 and hour<12:
        speak(f"Good morning sir . it's {tt}, ,So, how can i help you sir!")
        print(f"Jravis:Good morning sir . it's {tt}, ,So, how can i help you sir!")
            
    elif hour>= 12 and hour<16:
        speak(f"Good Afternoon sir . it's {tt}, ,So, how can i help you sir!")
        print(f"Jarvis:Good Afternoon sir . it's {tt}, ,So, how can i help you sir!")
            
    elif hour>16 and hour<20:
        speak(f"Good Evening sir. it's {tt}. So, how can i help you sir!")
        print(f"Jarvis:Good Evening sir. it's {tt}. So, how can i help you sir!")
            
    else:
        speak(f"Good night sir. it's {tt}. So, how can i help you sir!")
        print(f"Jarvis:Good night Sir. {tt}. So, how can i help you sir!")



if __name__ == "__main__":
    
    wishMe()
    while True:
        query = takeCommand()
        
            
            # logic for executing tasks based on query
        if 'who is' in query:
            speak("Searching Wikipedia.....")
            query = query.replace("who is", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print('Jarvis:',results)
            speak(results)

        elif 'YouTube' in query or 'Open YouTube' in query:
            speak('what should i search')
            x = takeCommand()
            speak('ok sir')
            webbrowser.open(f"https://www.youtube.com/results?search_query={x}")
                
        elif 'Google'in query:
            print("Jarvis:What should I search?")
            speak('what should i search')
            nope=takeCommand()
            speak('ok sir')
            webbrowser.open(f"https://www.google.com/search?q={nope}")
                
        elif "play" in query or " Jarvis play" in query or "jarvis next" in query:
                song = query.replace('play', '')
                speak("playing..")
                print("playing...")
                pywhatkit.playonyt(song)

        elif 'restart' in query:
            speak("Do you really want to restart this Pc sir?")
            ch = takeCommand()
            if "yes" in ch:
                        
                os.system("shutdown /r")
            else:
                speak("ok sir")
                
        elif 'shutdown' in query:
            speak("Do you really want to shutdown this PC sir?")
            ch = takeCommand()
            if "yes" in ch:
                        
                os.system("shutdown /s")
            else:
                speak("ok sir")
            
        elif 'who are you' in query:
            speak("Wait, i am introducing myself, My name is Jarvis, I am an Assistant made by python progarmming, i can do many works like playing music, opening progarms, opening youtube, searching on web and many more")
            print("Jarvis:Wait, i am introducing myself, My name is Jarvis, I am an Assistant made by python progarmming, I can do many works like playing music, opening progarms, opening youtube, searching on web and many more")

        elif 'tum kaise ho' in query:
            print("Jarvis:I am fine sir thank you, How are you")
            speak("I am fine sir thank you, How are you")

        elif 'hello' in query:
            print("Jarvis:Yes boss, What can i do for you")
            speak('Yes boss, What can I do for you')

        elif 'what is my name' in query:
            print("Jarvis:How can I forgot Your name, you are my honourable Developer Yathath Saxena")
            speak("How can I forgot Your name, you are my honourable Developer Yathath Saxena")


        elif 'what is the time' in query:
            speak('Sir, the time is')
            time()

        elif 'what is the date today' in query or 'what is the day' in query:
            speak("Sir, today is")
            date()

        elif 'who is my mother' in query or 'what is my mother name' in query:
            speak("Sir, yor mother name is Mrs. Pratibha Kanchan and you call him mummmy")
            print("Jarvis:Sir, yor mother name is Mrs. Pratibha Kanchan and you call him mummmy")

        elif 'thank you' in query or 'bahut acche' in query:
            print("Jarvis:Welcome Sir, by the way it is my pleasure")
            speak("welcome Sir, by the way it is my pleasure")

        elif 'main kahan rehta hoon' in query or 'where is my home' in query:
            print("Jarvis:Wait sir let me check.")
            speak("wait sir, let me check")
            print("Jarvis:Sir, We live in 370, Naika Mahen Jhusi  Allahabad  in the country of India.")
            speak("Sir, We live in 370, Naika    Mahen   Jhusi   Allahabad    in the country of India.")


        elif "joke" in query or 'tell me joke' in query or 'joke sunao' in query:
            lol=(pyjokes.get_joke())
            print("Jarvis:",lol)
            speak(lol)


        elif 'calculate' in query:
            client = wolframalpha.Client('P8AWYH-9JQ7EPJER4') 

            res = client.query(query)

            answer = next(res.results).text

            print('Jarvis:',answer)
            speak(answer)
                    



        elif "koi bhi gana bajao" in query:
            print("Jarvis:Ok Sir..")
            speak("OK Sir..")
            n = random.randint(0,14)
            print(n)

            music_dir = 'C:\\Users\\Pratibha\\Music'
            song = os.listdir(music_dir)
            print(song)

            os.startfile(os.path.join(music_dir,song[n]))

        elif "how are you"in query or "how Are you" in query or "How are you" in query:
            print("Jarvis:I am doing well, how about you?")
            speak("I am doing well, how about you?")
                    

        elif "I am also good" in query or "I am also fine" in query:
            print("Jarvis:That's great to hear from you")
            speak("That's great to hear from you")

        elif "what language do you speak" in query:
            print("Jarvis:I use to speak Python quite a bit")
            speak("I use to speak Python quite a bit")

        elif "what can you do for me" in query:
            print("Jarvis:I can do works which are behind your expectations.")
            speak("I can do works which are behind your expectations.")

        elif "lets chat" in query  or "can we chat"in query or 'can we talk' in query:
            speak("Why not sir.")
            chatbot.main()

        elif "I am sad" in query or "I am tired" in query:
            speak("Oh!, Should I play music to make you happy?")
            jk = takeCommand()
            if 'yes' in jk or 'yeah sure' in jk:
                speak('Ok Sir')
                tk = random.randint(0,14)
                print(tk)

                music_dir = 'C:\\Users\\Pratibha\\Music'
                song = os.listdir(music_dir)
                print(song)

                os.startfile(os.path.join(music_dir,song[tk]))
            else:
                speak('ok sir')

                    

        elif "tell me the weather of" in query or "weather of" in query:

            client = wolframalpha.Client('P8AWYH-9JQ7EPJER4') 

            res = client.query(query)

            ans = next(res.results).text


            print('Jarvis:',ans)
            speak(ans)
                    
        elif "quit" in query or 'goodbye' in query or "you can sleep now" in query:
            print("Jarvis:Quitting Sir. Thanks For Your Time")
            speak("Quitting Sir. Thanks For Your Time")
            exit()    
