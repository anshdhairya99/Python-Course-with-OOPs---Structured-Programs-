# Healthy Programmer :-------

# Question:--------------------------------------------------
# A officer complete the our job from 9am to 5pm:-----
# 9am - 5pm
# water - water.mp3 (3.5 litres) -Drank -log - Every 40 minutes
# Eyes - eyes.mp3 - every 30 min - eydone - log - every 30 min
# Physical activity - physical.mp3 every - 45 min Done - exdone - log

# Rules :--
# Used of pygame module to play the audio
#-----------------------------------------Code👇----------------------------------------------- 


from pygame import mixer
from datetime import datetime 
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("mylogs.txt","a")as f:
        f.write(f"{msg} {datetime.now()}\n")
if __name__ == '__main__':
    #musiconloop("water.mp3.mp3","stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 5
    exsecs = 10
    eyesecs = 20
while True:
    if time() - init_water > watersecs:
        print("Water drinking time. Enter ' drank' to stop the alarm")
        musiconloop('water.mp3.mp3','drank')
        init_water = time()
        log_now("Drank water at")

    if time() - init_eyes  > eyesecs:
        print("Eyes Exercise time. Enter 'done' to stop the alarm")
        musiconloop('eyes.mp3.mp3','done eyes')
        init_eyes = time()
        log_now("Eyes Relaxed at")

    if time() - init_exercise > exsecs:
        print("Physical Activity Time. Enter ' donephy' to stop the alarm")
        musiconloop('physical.mp3.mp3','donephy')
        init_exercise = time()
        log_now("Physical Activity done at")    



        