# reads data from stratologger to ensure and is below 5 feet. This program then turns on and moves three feet away from drop site.
# then it moves to main and listens for next instructions

import speech_recognition as sr 
import cv2 as cv
import threading

commands = [None] * 100

def listen():
    #https://www.thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python

# create a speech recognition object
    r = sr.Recognizer()

    # a function that splits the audio file into chunks
    # and applies speech recognition
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        audio_data = r.record(source, duration=5) # change duration to however long you want the recording to last 
        print("Recognizing...")
        # convert speech to text
        text = r.recognize_google(audio_data)
        print(text)   #instead of print store in a string and use if statements to create .contains situations
        return text

def recieveVideo():
    capture = cv.VideoCapture(0)  #change this to video
    while True:
        isTrue, frame = capture.read()  # capture.read reads in video frame by frame and returns the frame and a boolean that says whether the frame was succesfully read in or not
        cv.imshow('Video', frame)

        if cv.waitKey(20) & 0xFF==ord('d'):   # if d is pressed break out of loop and stop displaying video
            break

    capture.release()
    cv.destroyAllWindows()
    cv.waitKey(0)

def alwaysListen():  #only goes for 4 times for some reason (have to fix later)
    while(listen().find('stop') == -1):
        r = sr.Recognizer()

        with sr.Microphone() as source:
            audio_data = r.record(source, duration = 2) 
            print("Recognizing...")
            try:
                text = r.recognize_google(audio_data)
                print(text)  
                commands.append(text) 
            except:
                text = "...."
                print("....")

    print(commands)
    return commands

def runSimul():
    threading.Thread(target=alwaysListen).start()
    threading.Thread(target=recieveVideo).start()


from time import sleep

comm = alwaysListen()
for i in comm:
    print(i)
