import speech_recognition as sr
import pyttsx3 
import time

def Listen():
    r = sr.Recognizer() 
    count = 0

    while(count < 1):    
      
    # Exception handling to handle
    # exceptions at the runtime
        try:
          
        # use the microphone as source for input.
            with sr.Microphone() as source2:
              
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
                r.adjust_for_ambient_noise(source2, duration=0.2)
              
            #listens for the user's input 
                audio2 = r.listen(source2)
              
            # Using google to recognize audio
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
  
                #print("Did you say "+MyText)
                count += 1
                return "" + MyText            # make this into a method so that it will return string and put into an array, everytime called
              
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            count += 1
          
        except sr.UnknownValueError:
            print("unknown error occured")
            count += 1

 # Make commands go into a text file and store it somewhere or an array

#count = 0  #make it so that if more orders are to come say a specific word like wait at the end so that it runs again in like 5 seconds
commands = [None] * 100  #make it wait until it hears a command before going to next line
for i in range(2):
    commands[i] = Listen()   
    time.sleep(3)

print(commands)


# while command does not contain stop
# listen and store command
# do a bunch of if statements on commands (forward, backward, grab, release, turn right, turn left, stop)