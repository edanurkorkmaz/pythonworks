from datetime import datetime, timedelta
import time
import pygame

def alarm_cal():

    pygame.init()
    pygame.mixer.music.load("c:/Users/Topfiyt3/Desktop/alarm.mp3") 
    pygame.mixer.music.play()


simdi = datetime.now()
alarm_zamani = simdi + timedelta(seconds=5)

print("Alarm zamanı:", alarm_zamani)


while datetime.now() < alarm_zamani:
    alarm_cal()
    
time.sleep(10)




