import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
import os

# Text-to-speech setup
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Speech recognizer
recognizer = sr.Recognizer()

# ✅ Web and App Command Maps
websites = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "twitter": "https://www.twitter.com",
    "facebook": "https://www.facebook.com",
    "whatsapp": "https://web.whatsapp.com"
}

apps = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "vs code": r"C:\Users\Rupashree\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    "whatsapp": r"C:\Users\Rupashree\AppData\Local\WhatsApp\WhatsApp.exe"
}

def listen_command():
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening for your command.")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
        except sr.RequestError:
            speak("Could not request results; check your internet connection.")
        return ""

def process_command(command):
    for key in websites:
        if key in command:
            speak(f"Opening {key}")
            webbrowser.open(websites[key])
            return

    for key in apps:
        if key in command:
            speak(f"Launching {key}")
            try:
                subprocess.Popen(apps[key])
                return
            except Exception as e:
                speak(f"Failed to launch {key}")
                print(f"Error: {e}")
                return

    speak("Command not recognized.")

# ✅ Main loop
if __name__ == "__main__":
    while True:
        cmd = listen_command()
        if "exit" in cmd or "quit" in cmd:
            speak("Goodbye!")
            break
        process_command(cmd)
