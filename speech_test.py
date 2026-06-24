import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("What would you like to change from speech to text?")

    recognizer.adjust_for_ambient_noise(source, duration=1)
    audio_data = recognizer.listen(source)

    try:

        text= recognizer.recognize_google(audio_data)
        print(f"Text: {text}")
    
    except sr.UnknownValueError:
        print("Unknown error.")
    except sr.RequestError:
        print("Request error.")

