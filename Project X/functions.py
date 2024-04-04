import random
from discord.ext import commands
from discord.utils import get


import json

# Load scores from file at start
try:
    with open('scores.json', 'r') as f:
        scores = json.load(f)
except FileNotFoundError:
    scores = {}

def get_random_number():
    return random.randint(1, 100)

def battleBattleRoll(words, ctx):
    if len(words) > 1 and words[1].startswith("<") and words[1].endswith(">"):
        opponent = words[1]

        authorRoll = get_random_number()
        opponentRoll = get_random_number()

        server_id = str(ctx.guild.id)
        if server_id not in scores:
            scores[server_id] = {}

        if authorRoll > opponentRoll:
            winnnerDisplay = ctx.author.display_name
            winner = ctx.author.mention
            loserDisplay = ctx.message.mentions[0].display_name
            loser = opponent
        elif authorRoll < opponentRoll:
            winnnerDisplay = ctx.message.mentions[0].display_name
            loserDisplay = ctx.author.display_name
            winner = opponent
            loser = ctx.author.mention
        else:
            return f"{ctx.author.mention} and {opponent} both rolled {authorRoll}. It's a tie!"

        # Update scores
        scores[server_id][winnnerDisplay] = scores[server_id].get(winnnerDisplay, 0) + 1
        scores[server_id][loserDisplay] = scores[server_id].get(loserDisplay, 0) - 1

        # Save scores to file
        with open('scores.json', 'w') as f:
            json.dump(scores, f)

        return f"{ctx.author.mention} rolled {authorRoll}, {opponent} rolled {opponentRoll}. {winner} wins!"
    else:
        return "You must mention a user to start a battle."
    
def get_scores(ctx):
    server_id = str(ctx.guild.id)
    if server_id not in scores:
        return "No scores yet!"
    return "\n".join([f"{user}: {score}" for user, score in scores[server_id].items()])