import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import pyjokes


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    
    elif hour>=12 and hour <18:
        speak("Good Afternoon")
    
    else:
        speak("Good Eavening")
    
    speak("I am Mani Sir. Please tell me how may i help you?")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 3
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        #print(e)

        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server= smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kaivalyam19@gmail.com', 'bdpgygtbxlvojafi')
    server.sendmail('kaivalyam19@gmail.com', to , content)
    server.close()

if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()
    
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif ' open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'open college login' in query:
            webbrowser.open("vtop.vitbhopal.ac.in/vtop/initialProcess")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'chrome' in query:
            codePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)
        
        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'play' in query:
            speak('searching youtube')
            song = query.replace('play', '')
            speak('playing'+song)
            pywhatkit.playonyt(song)
        
        elif 'email to me' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "alphacharlie1807@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry, i failed to send the Email")