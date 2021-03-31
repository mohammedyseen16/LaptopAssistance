import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import wolframalpha
import webbrowser
import os 
import ctypes
import smtplib
from time import ctime
import time
import turtle
from gtts import gTTS
from urllib.request import urlopen
import jarvis
import json
import requests

 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")
    
    speak("I am Jack Sir. Please tell me how can I help you")

def takeCommand():
    #it takes microphone input yass
    r = sr.Recognizer() 
    print("Listening...")
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.energy_threshold = 5000
        audio = r.listen(source)
  
    try: 
        #print("Recognizing..")
        query = r.recognize_google(audio, language ='en-in')
        print(query)
 
    except Exception as e:
        print(e)
         
        return "None"
    return query

#credentials
def sendEmail(to , content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('jackrourke17045@gmail.com', 'asiftabassum')
    server.sendmail('yaseen17045@gmail.com', to, content)
    server.close()

if __name__ == '__main__':
    
    #wishMe() 
    while True:
        query = takeCommand().lower()

    #logic for executing a task
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results) 
      
        elif 'open google' in query:
            webbrowser.open('http://www.google.com')
            speak("opening Google sir..")
 
        elif 'about' in query:
            webbrowser.open('http://www.google.com/{query}')
            
        elif 'open youtube' in query:
            webbrowser.open('http://www.youtube.com')
            speak("opening youtube sir..")

        elif 'open chrome' in query:
            webbrowser.open('http://chrome.google.com')
            speak("opening chrome sir..")
        
        elif 'how are you' in query:
            speak("I am fine Sir, Thank you")
            speak("How are you, Sir")

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query
 
        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")
 
        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif 'open chrome app' in query:
            webbrowser.open('http://www.google.com')
            speak("opening chrome sir..")
        
        elif 'open mail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/")  
            speak("opening Gmail sir..")
  
        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/")
            speak("opening Gmail sir..")

        elif 'open amazon prime' in query:
            webbrowser.open('http://www.primevideo.com')
            print("Opening Amazon Prime sir")
            speak("opening Amazon Prime sir..")
            

        elif 'open prime' in query:
            webbrowser.open('http://www.primevideo.com')
            print("opening Amazon Prime sir..")
            speak("opening Amazon Prime sir..")
        
        elif 'open facebook' in query:
            webbrowser.open('https://www.facebook.com/')
            print("opening Facebook sir..")
            speak("opening facebook sir..")

        elif 'open instagram' in query:
            webbrowser.open('https://www.instagram.com/')
            print("opening instagram sir..")
            speak("opening instagram sir..")

  
        elif 'open netflix' in query:
            webbrowser.open('https://netflix.com/')
            print("Opening Netflix sir")
            speak("opening Netflix sir..")
        
        elif 'open hotstar' in query:
            webbrowser.open('https://www.hotstar.com/in')
            speak("opening hotstar sir..")

        elif 'open spotify' in query:
            webbrowser.open('https://open.spotify.com/?_gl=1*6qnmrl*_gcl_aw*R0NMLjE2MTcwODM4MDAuQ2owS0NRanc5WVdEQmhEeUFSSXNBRHQ2c0dhOWFIMnV5dXNMSjJhR3BvZnl1Z0JtQjZIQ1VfMTZKRC1ma3ZnRHpMcXNXcThqYWgyUndXNGFBdEtqRUFMd193Y0I.*_gcl_dc*R0NMLjE2MTcwODM4MDAuQ2owS0NRanc5WVdEQmhEeUFSSXNBRHQ2c0dhOWFIMnV5dXNMSjJhR3BvZnl1Z0JtQjZIQ1VfMTZKRC1ma3ZnRHpMcXNXcThqYWgyUndXNGFBdEtqRUFMd193Y0I.&_ga=2.56352430.485174340.1617036939-166875349.1609187154&_gac=1.81180773.1617083800.Cj0KCQjw9YWDBhDyARIsADt6sGa9aH2uyusLJ2aGpofyugBmB6HCU_16JD-fkvgDzLqsWq8jah2RwW4aAtKjEALw_wcB')
            speak("opening spotify sir..")
        
        elif 'open github' in query:
            webbrowser.open("github.com") 
            speak("opening github sir..")
        elif 'open myntra' in query:
            webbrowser.open("https://www.myntra.com/") 
            speak("opening myntra sir..")
            speak("enjoy shopping sir")
            speak("sir, do you want me to help you for shopping!")
        
 
        elif 'play music' in query:
            music_dir = 'C:\\Users\\Mohammed Yaseen\\Music\\music'
            songs = os.listdir(music_dir)
            speak("There you go sir.. playing your favourite")
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'next song' in query:
            music_dir = 'C:\\Users\\Mohammed Yaseen\\Music\\music'
            songs = os.listdir(music_dir)
            speak("There you go sir.. playing next song")
            os.startfile(os.path.join(music_dir, songs[1]))
          
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'sir, the time is {strTime}')
            print(strTime)
        
        elif 'open notepad plus plus' in query:
            speak("There you go sir opening Notepad plus plus..")
            notePath = "C:\\Program Files\\Notepad++\\notepad++.exe"
            os.startfile(notePath)

        elif 'open notepad' in query:
            NotePath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(NotePath)
    
        
        elif 'open windows word' in query or 'open word' in query:
            wordpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007.lnk"
            speak(f'there you go sir! opening windows word')
            os.startfile(wordpath)

        elif 'open visual studio code' in query or 'open code' in query: 
            codePath = "C:\\Users\\Mohammed Yaseen\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak(f'there you go sir! opening visual studio code')
            os.startfile(codePath)
        
        elif 'open power point' in query or 'open powerpoint' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office PowerPoint 2007.lnk"
            speak(f'there you go sir! opening powerpoit')
            os.startfile(codePath)
 
        elif 'power point presentation' in query:
            speak("opening Power Point presentation")
            power = r" "
            os.startfile(power)
        
        elif 'taron ke shahar' in query or 'taron ki shehar' in query:  
            CodePath = "C:\\Users\\Mohammed Yaseen\\Music\\music\\Taaron Ke Shehar - Neha Kakkar.mp3"
            speak(f'there you go sir!')
            os.startfile(CodePath)
        
        elif 'tujhe kitna' in query:
            sog1 ="C:\\Users\\Mohammed Yaseen\\Desktop\\desktop\\songs\\09 - Tujhe Kitna Chahein Aur - Kabir Singh (2019).mp3"
            speak(f'there you go sir!')
            os.startfile(sog1)
            

        elif 'bekhayali' in query:
            sog2 ="C:\\Users\\Mohammed Yaseen\\Desktop\\desktop\\songs\\03 - Bekhayali (Arijit Singh) - Kabir Singh (2019).mp3"
            speak(f'there you go sir!')
            os.startfile(sog2)
        
        elif 'humko tum mil gaye' in query:
            sog3 ="C:\\Users\\Mohammed Yaseen\\Desktop\\desktop\\songs\\Humko Tum Mil Gaye - Vishal Mishra.mp3"
            speak(f'there you go sir!')
            os.startfile(sog3)
        
        elif 'aaj bhi' in query:
            sog4 ="C:\\Users\\Mohammed Yaseen\\Desktop\\desktop\\songs\\Aaj Bhi - Vishal Mishra.mp3"
            speak(f'there you go sir!')
            os.startfile(sog4)
        
        
        #google search------- 
        elif "where is" in query:
            query = query.split(" ")
            location = query[2]
            speak("Hold on sir, I will show you where " + location + " is.")
            webbrowser.open("http://www.google.nl/maps/place/" + location + "/&amp;")
        
        elif 'jarvis search' in query: 
            speak("What Should I search sir?")
            content1 = takeCommand()
            webbrowser.open("http://www.google.com/search?q="+ content1)
            speak("just a second sir!")

        elif "hey jarvis" in query or "hi jarvis" in query: 
            speak("yes sir")
            query = takeCommand() 
            speak("in a second sir!")
            webbrowser.open("http://www.google.com/search?q=" + query)
    
        elif "what" in query:
            query = query.split(" ")
            location = query[2]+' '+query[3]+' '+query[4]
            speak("sir According to google " + location + " is.")
            webbrowser.open("http://www.google.com/search?q="+ location)
      
        elif "song in" in query:
            query = query.split(" ")
            location = query[1]+' '+query[2]
            speak("opening"+location+"song in youtube")
            webbrowser.open("https://www.youtube.com/results?search_query="+ location)
        
        elif "in youtube" in query:
            query = query.split(" ")
            location = query[1]+' '+query[2]
            speak("opening"+location+"song in youtube")
            webbrowser.open("https://www.youtube.com/results?search_query="+ location)

          

        #-----------------------------------------------------
        
        elif 'email to yaseen' in query:
            try:
                speak("What Should I say sir?")
                content = takeCommand()
                to  = "yaseen17045@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
                speak("Anything else sir")
            except Exception as e:
                print(e)
                speak("sorry")
            
        elif 'email to wasim' in query:
            try:
                speak("What Should I say sir?")
                content = takeCommand()
                to  = "mailto:wmohammed693@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
                speak("Anything else sir")
            except Exception as e:
                print(e)
                speak("sorry")

        elif 'hey jack' in query:
            speak('Hi sir how can i help you!')
        
        elif 'hi jack' in query:
            speak('Hi sir how can i help you!')
        
        elif 'hello jack' in query:
            speak('Hi sir how can i help you!')

        elif 'jack' in query:
            speak('Hi sir how can i help you!')
        
        elif 'hey jack can you do me a favour' in query:
            speak('Hi sir how can i help you!')
        
        elif 'thank you jack' in query:
            speak('Anytime sir..')
            speak("If you need anything i will be here")

        elif 'thank you' in query:
            speak('Anytime sir')
        
        elif 'jack' in query:
            speak('yes sir')
        
        elif 'do you miss tony stark' in query:
            speak('yes sir')
            speak('But i hate Thanos')

        elif 'do you miss iron man' in query:
            speak('yes sir')
            speak('But i hate Thanos')
        
        elif 'message your girlfriend' in query:
            speak("Sorry, sir i don't have girlfriend")
            speak("instead do you want me to message your's sir?")
        
        elif 'no thank you' in query:
            speak('Ok sir')

        elif 'weather' in query:
            webbrowser.open("https://www.google.com/search?q=today%27s%20weather&gws_rd=ssl") 
            speak('Showing results on current weather sir..')
  
        elif "who made you" in query or "who created you" in query:
            speak("you sir, you created me")
            speak("Thank you sir")

        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")
        
        elif 'start an instant meeting' in query:
            speak("ok sir opening google meet")
            webbrowser.open("https://meet.google.com/_meet/jrq-cvbb-dmm?ijlm=1617121727687&adhoc=1&hs=187") 
 
        elif "who are you" in query:
            speak("I am your virtual assistant created by team Yaseen")

        elif "stop embarrassing me" in query:
            speak("my apologies sir")

        elif "everyone are laughing" in query:
            speak("my apologies sir")

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "C:\\Users\\Mohammed Yaseen\\Downloads\\pexels-vlad-alexandru-popa-1402787.jpg",
                                                       0)
            speak("Background changed succesfully")
        
        elif "sleep" in query:
            speak("Thank you sir i will go to sleep") 

        elif 'wake up jarvis' in query:
            speak("ok sir i got up, what can i do sir") 
        
        elif "quit jarvis" in query or "exit" in query:
            exit()
        
        
        

        

        
        



















        

            
        




        
 
     
  
 
 
                 
