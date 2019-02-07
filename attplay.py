
import time

import speech_recognition as sr
from time import ctime
import time
import os
#from gtts import gTTS
from win32com.client import constants
import win32com.client
#from random import randrange
value=0   


def speak(audioString):
    print("B: "+audioString)
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(audioString)
	
	
    

def recordAudio(rollNo):
    # Record Audio
    r = sr.Recognizer()
    data = ""
    while len(data)==0:
        with sr.Microphone(device_index=1) as source:
            r.energy_threshold=180  # minimum audio energy to consider for recording
            #r.dynamic_energy_threshold = True
            #r.dynamic_energy_adjustment_damping = 0.15
            r.dynamic_energy_ratio = 0.1
            #r.pause_threshold = 0.8  # seconds of non-speaking audio before a phrase is considered complete
            #r.operation_timeout = None  # seconds after an internal operation (e.g., an API request) starts before it times out, or ``None`` for no timeout

            r.phrase_threshold = 0.01  # minimum seconds of speaking audio before we consider the speaking audio a phrase - values below this are ignored
            #(for filtering out clicks and pops)
            #r.non_speaking_duration = 0 # seconds of non-speaking audio to keep on both sides of the recording

            r.adjust_for_ambient_noise(source,duration=1)
            print(str(rollNo))
            speak(str(rollNo))
            
            audio = r.listen(source,phrase_time_limit=1)
        
        try:
            #print("Audio Recorded")
            # Uses the default API key
            # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            data = r.recognize_google(audio,language='en-IN')
            print("You said: " + data)
        except sr.UnknownValueError:
            speak("Google Speech Recognition could not understand audio")
            check=1
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            
    return data
	

				
       
# initialization
#time.sleep(2)
speak("Response to your attendance")
i=1
while i<=5:
    data = recordAudio(i) #input();  
    
    i=i+1
    	
