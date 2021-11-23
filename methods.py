import speech_recognition as sr 
import cv2 as cv

def listen():

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
        print(text)

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

