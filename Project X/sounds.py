import discord
import random
import time
import os

removeSound = "sounds/remove.mp3"
potatis = "sounds/potatis.mp3"
redSun = "sounds/redSun.mp3"
redsun2 = "sounds/redSun2.mp3"


differentSound = [removeSound, potatis, redSun, redsun2]
last_played = {sound: 0 for sound in differentSound}
cooldown = 60

def discordPlayMp3(soundPath):
    return discord.FFmpegPCMAudio(executable="ffmpeg", source=soundPath)