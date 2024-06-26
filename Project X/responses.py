import asciiArt
from discord.ext import commands
import asyncio
import functions
import sounds
from hangman import hangman
from gtts import gTTS

async def play(ctx, soundPath: str):
    # Ensure the bot is in a voice channel
    if ctx.author.voice is None:
        await ctx.send("You're not in a voice channel!")
        return

    # Connect to the voice channel
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
        await voice_channel.connect()
    else:
        await ctx.voice_client.move_to(voice_channel)

    # Play the audio file
    audio_source = sounds.discordPlayMp3(soundPath)
    if not ctx.voice_client.is_playing():
        ctx.voice_client.play(audio_source, after=lambda e: print('done', e))

    # Wait for the audio to finish, then disconnect
    while ctx.voice_client.is_playing():
        await asyncio.sleep(1)
    await ctx.voice_client.disconnect()


async def get_response(ctx, user_input: str) -> str:
    lowered_input = user_input.lower()
    words = lowered_input.split()

    if words[0] == "king":
        await play(ctx, sounds.removeSound)
        return asciiArt.xiJingPingArt
    
    if words[0] == "roll":
        return f"{ctx.author.mention} Has rolled a sexy {functions.get_random_number()}"
    
    if words[0] == "bakugan":
        return functions.battleBattleRoll(words, ctx)
    
    if words[0] == "hangman":
        return await hangman.hangman(ctx)
    if words[0] == "score":
        return functions.get_scores(ctx)
    if words[0] == "tts":
        lang = "en"
        text = " ".join(words[1:])
        tts = gTTS(text=text, lang=lang, slow=False)
        tts.save("speech.mp3")
        await play(ctx, "speech.mp3")
        return "Playing text to speech"
