import time
import speech_recognition as sr
import os

#Needs a good mic!
def voiceInput():
    r = sr.Recognizer() 
    mic = sr.Microphone()
    with mic as source:
        audio = r.listen(source)
    mytext = r.recognize_google(audio)
    return (mytext)

while (True):
    os.system("cls")
    print("""
1- say 'kilogram' to convert from pounds to kgs.
2- say 'pounds' to convert from kgs to pounds.
3- say 'Exit' to exit the program.
    """)
    print("Listening...")
    firstInput = voiceInput().lower()
    print (firstInput)


    if firstInput == "kilogram":
        print("you have selected pounds to kgs.")
        print("Say your weight in pounds.")
        pounds = int(voiceInput())
        print (f"You said '{pounds}'")
        kgs = pounds/2.2
        print(f"your weight in kgs = {kgs}")
    elif firstInput == "pounds":
        print("you have selected kgs to kgs.")
        print("Say your weight in kgs.")
        kgs = int(voiceInput())
        print (f"You said '{kgs}'")
        pounds = kgs*2.2
        print(f"your weight in pounds = {pounds}")
    elif firstInput == "exit":
        exit(0)
    else:
        print("Unkown input!\nTry again")
        time.sleep(5)

