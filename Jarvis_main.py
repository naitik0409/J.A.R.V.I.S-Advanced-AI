import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# Core imports with error handling
try:
    import pygame
    import pyttsx3
    import speech_recognition as sr
    import datetime
    import pyautogui
    import pywhatkit
    import wikipedia
    import pyjokes
    import cv2
    import psutil
    import sys
    import time
    from datetime import date
    import calendar
except Exception as e:
    print(f"Error importing core modules: {e}")
    sys.exit(1)

# Initialize pygame properly
try:
    pygame.init()
    if pygame.mixer:
        pygame.mixer.init()
except Exception as e:
    print(f"Warning: Could not initialize pygame: {e}")

# Initialize text-to-speech with better error handling
def initialize_tts():
    try:
        engine = pyttsx3.init("sapi5")
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[0].id)
        engine.setProperty("rate", 170)
        return engine
    except Exception as e:
        print(f"Error initializing text-to-speech: {e}")
        sys.exit(1)

engine = initialize_tts()

def speak(audio):
    try:
        engine.say(audio)
        engine.runAndWait()
    except Exception as e:
        print(f"Error speaking: {e}")

def takeCommand():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening.....")
            r.pause_threshold = 1
            r.energy_threshold = 300
            audio = r.listen(source, 0, 4)

        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
        return query.lower()
    except sr.RequestError:
        print("Could not request results; check your internet connection")
        return "None"
    except sr.UnknownValueError:
        print("Say that again")
        return "None"
    except Exception as e:
        print(f"Error in speech recognition: {e}")
        return "None"

def setup_directories():
    """Create necessary directories"""
    try:
        dirs = ['data', 'logs', 'temp']
        for dir_name in dirs:
            os.makedirs(dir_name, exist_ok=True)
    except Exception as e:
        print(f"Error creating directories: {e}")

def listen():
    query = takeCommand()
    return query

if __name__ == "__main__":
    try:
        setup_directories()
        print("Jarvis initialized successfully!")
        speak("Jarvis is ready")
        
        while True:
            query = listen()
            if "wake up" in query:
                try:
                    from GreetMe import greetMe
                    greetMe()
                    
                    while True:
                        query = listen()
                        
                        if "go to sleep" in query:
                            speak("Ok sir, you can call me anytime")
                            break
                        
                        # Your existing command handling code here...
                        
                except Exception as e:
                    print(f"Error in command execution: {e}")
                    speak("I encountered an error. Please try again.")
            
            elif "exit" in query or "quit" in query:
                speak("Goodbye!")
                sys.exit(0)
                
    except Exception as e:
        print(f"Critical error: {e}")
        speak("Critical error occurred. Shutting down.")
        sys.exit(1) 