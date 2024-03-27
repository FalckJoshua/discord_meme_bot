import random
from . import hangmanArt
from . import hangmanWordList
from discord.ext import commands
import asyncio

word_list = hangmanWordList.word_list

async def hangman(ctx):
    choosen_word = random.choice(word_list)

    correct_guess = []
    wrong_guess = []

    for letter in choosen_word:
        correct_guess.append("_")
    i = 0
    previous_messages = []
    while(i < 7 and correct_guess != list(choosen_word)):
        new_messages = []
        guess_message = await ctx.send("Guess a letter: ")
        new_messages.append(guess_message)
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content.startswith('%g')
        message = await ctx.bot.wait_for('message', check=check)
        guess = message.content.lower().strip('%g')
        correct = False
        for position in range(len(choosen_word)):    
            letter = choosen_word[position]
            if letter == guess:
                correct_guess[position] = letter
                correct = True
        if not correct and guess not in wrong_guess:
            wrong_guess.append(guess)
            i += 1
        new_messages.append(await ctx.send(f"correct_guess{correct_guess}"))
        new_messages.append(await ctx.send(f"Wrong guesses {wrong_guess}"))
        new_messages.append(await ctx.send(f"Attempt left {7 - i}{hangmanArt.stages[7-i]}"))

        # Delete previous messages
        deletion_tasks = [msg.delete() for msg in previous_messages]
        await asyncio.gather(*deletion_tasks)
        previous_messages = new_messages

    if (correct_guess == list(choosen_word)):
        await ctx.send("You win, uwu intelligent human")
    else:
        await ctx.send("You lose u idiot")
        await ctx.send(f"The word was {choosen_word}")