import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    """This function will greet the user according to the time."""
    hour = datetime.datetime.now().hour

    if hour >= 0 and hour < 12:
        speak("Assalam O ALaikum !Good Morning Sir!")

    elif hour >= 12 and hour < 18:
        speak("Assalam O ALaikum !Good Afternoon Sir!")

    else:
        speak("Assalam O ALaikum !Good Evening Sir!")

    speak("Sir I am Jarvis, your AI Assistant. How may I help you Sir!")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.energy_threshold = 0
        r.pause_threshold = 1
        audio = r.listen(source, 2)

    # try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")

    # except Exception as e:
    #     print("Say that again please...\n")
    #     return "None"
    return query
if __name__ == '__main__':

    wishMe()
    while True:
        query = takeCommand()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            print("Opening Youtube for you...")
            speak("Opening Youtube for you...")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            print("Opening Google for you...")
            speak("Opening Google for you...")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            print("Opening Stack Over Flow for you...")
            speak("Opening Stack Over Flow for you...")
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir! The time is {strTime}")