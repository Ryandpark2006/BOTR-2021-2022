# doc to transmit and take videos

import cv2 as cv

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

recieveVideo()

