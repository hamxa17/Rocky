The App:

Rocky happens to be inspired by an alien in the movie Project Hail Mary. The app itself is nothing huge. Just takes your microphone input and coverts the spoken words into text format.

The process:

-It uses Google Cloud API for speech recognition
-Threading was used to seamlessly listen and grab the information from Google Cloud API.
-Tkinter was used for the app's Frontend UI.
-First, I built the Rocky app class in which:
1. I defined __init__ to initialise the main window settings and to draw the frontend ui(Microphone button, output boc, etc.).
2. Then I defined listening in which the app starts to listen for the audio input as soon as the "speak" button is pressed. Previously mentioned threading was used here.
3. After that, process_audio was defined in which the thread captures the audio and translates it.
4. Following that, update_output_text was defined which just opens the text box, deletes any existing message, updates the new text into the text box.
5. lastly, reset ui was defined which just resets the button to its restiong state.
-The last bit of the program is to ensure a proper runtime.

Requirements:

Of course, you would have to ensure python is installed in your PC. Along with the you will need to install some necessary libraries: Speech Recognition library and PyAudio(Required for microphone access)

How to install both:
Open your terminal(or Command Prompt) and run these:

# Install speech recognition library
pip install SpeechRecognition

# Install PyAudio
pip install pyaudio