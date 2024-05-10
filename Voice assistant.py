import speech_recognition as sr
import pyttsx3
import requests
import datetime
import json

# Initialize the recognizer and the pyttsx3 engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Speak out the given text."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for commands."""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("I didn't understand that.")
        return None
    except sr.RequestError:
        speak("Failed to obtain results.")
        return None

def process_command(command):
    """Process the command."""
    if 'time' in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    elif 'weather' in command:
        get_weather()
    elif 'stop' in command:
        speak("Goodbye!")
        return False
    else:
        speak("Sorry, I can't help with that yet.")
    return True

def get_weather():
    """Get weather information from an API."""
    api_key = "your_openweathermap_api_key"  # Replace with your actual API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "your_city_name"  # Replace with your actual city name
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    weather_data = response.json()
    if weather_data["cod"] != "404":
        main = weather_data["main"]
        temperature = main["temp"] - 273.15  # Convert from Kelvin to Celsius
        humidity = main["humidity"]
        weather_description = weather_data["weather"][0]["description"]
        weather_report = f"Temperature: {temperature:.2f}°C, Humidity: {humidity}%, Description: {weather_description}"
        speak("Here is the weather report:")
        speak(weather_report)
    else:
        speak("City not found.")

def main():
    speak("Hello, I am your assistant. What can I do for you today?")
    running = True
    while running:
        command = listen()
        if command:
            running = process_command(command)

if __name__ == "__main__":
    main()
