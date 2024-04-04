import discord
import random
import time
import os

removeSound = "Project X/sounds/remove.mp3"
potatis = "Project X/sounds/potatis.mp3"
redSun = "Project X/sounds/redSun.mp3"
redsun2 = "Project X/sounds/redSun2.mp3"


differentSound = [removeSound, potatis, redSun, redsun2]
last_played = {sound: 0 for sound in differentSound}
cooldown = 60

def discordPlayMp3(soundPath):
    global last_played
    current_time = time.time()

    available_sounds = [sound for sound in differentSound if current_time - last_played[sound] > cooldown]
    if not available_sounds:
        return None

    randomSound = random.choice(available_sounds)
    last_played[randomSound] = current_time

    if not os.path.isfile(randomSound):
        print(f"File not found: {randomSound}")
        return None
    
    return discord.FFmpegPCMAudio(executable="ffmpeg", source=randomSound)