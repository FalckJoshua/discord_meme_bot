import random
from discord.ext import commands

def get_random_number():
    return random.randint(1, 100)

def battleBattleRoll(words, ctx):
    if len(words) > 1 and words[1].startswith("<") and words[1].endswith(">"):
        opponent = words[1]

        authorRoll = get_random_number()
        opponentRoll = get_random_number()
        print(authorRoll)
        print("hello")
        print(opponentRoll)
        if authorRoll > opponentRoll:
            return f"{ctx.author.mention} rolled {authorRoll}, {opponent} rolled {opponentRoll}. {ctx.author.mention} wins!"
        elif authorRoll < opponentRoll:
            return f"{ctx.author.mention} rolled {authorRoll}, {opponent} rolled {opponentRoll}. {opponent} wins!"
        else:
            return f"{ctx.author.mention} and {opponent} both rolled {authorRoll}. It's a tie!"
    else:
        return "You must mention a user to start a battle."