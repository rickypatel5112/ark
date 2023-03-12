import datetime

import pyttsx3
import speech_recognition as sr


def text_to_speech(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    audio_file = "static/audiofile.wav"
    engine.save_to_file(text, audio_file)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        return "Good Morning!"

    elif hour>=12 and hour<18:
        return "Good Afternoon!"   
    else:
        return "Good Evening!" 
     

def speech_to_text():

    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:    
        query = r.recognize_google(audio, language='eng')

        print(query)

    except Exception as e: 
        return "None"
    return query


# def proc_queries():
#         query = speech_to_text().lower()

#         # Logic for executing tasks based on query
#         if 'hello can you hear me' in query:
#             return 'I can hear you perfectly! Please, how may I help you?'
#         if 'how are you' in query:
#             return 'I am doing well, thank you for asking'       
#         if 'the time' in query:
#             strTime = datetime.datetime.now().strftime("%H:%M:%S")    
#             return f"Sir, the time is {strTime}"
#         if 'is it a good idea to do programming all day' in query:
#             return 'Of course, it is a good idea to do so!'
#         if 'Tell Ujjwal and Saumya they have huge heads' in query:
#             return 'Of course, Hey Ujjwal and Saumya, you two have huge heads!'
#         if 'bye stop the program' in query:
#             return 'Okay, have a good day sir!'
#         else:
#             return "Sorry, I don't get it"
        