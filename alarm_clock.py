from playsound import playsound
import time
import threading

user = int(input("hány másodperc múlva állítsunk ébresztőt?: "))

def alarm():
    playsound("clock.wav")

thread = threading.Thread(target=alarm)
thread.start()

while user > 0:
        
    time.sleep(1)
    user -= 1
    
    if user == 0:
        snooze = str(input("Leállításhoz írjon egy K betűt: "))
        if snooze == "K":
            break



    
    