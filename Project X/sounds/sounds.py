import discord
import random
import time

removeSound = "sounds/remove.mp3"
potatis = "sounds/potatis.mp3"
redSun = "sounds/redSun.mp3"
redsun2 = "sounds/redSun2.mp3"


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
    
    return discord.FFmpegPCMAudio(executable="ffmpeg", source=randomSound)

