# SpeechRecognition Example
# This example shows how to use SpeechRecognition with Google Speech Recognition
# It will convert speech recorded from the microphone to text
# This is a modified version of this example: https://github.com/Uberi/speech_recognition/blob/master/examples/microphone_recognition.py
# Author: Uberi/Audun Liberg


# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr

# Obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# Recognize speech using Google Speech Recognition
try:
    # For testing purposes, we're just using the default API key
    # To use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY") instead of `r.recognize_google(audio)`
    print('Google Speech Recognition thinks you said:\n\n\t"' + r.recognize_google(audio) + '"')
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
