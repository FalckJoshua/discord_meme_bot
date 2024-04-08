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
        if winnnerDisplay not in scores[server_id]:
            scores[server_id][winnnerDisplay] = {"score": 0, "wins": 0, "losses": 0}

        if loserDisplay not in scores[server_id]:
            scores[server_id][loserDisplay] = {"score": 0, "wins": 0, "losses": 0}

        scores[server_id][winnnerDisplay]["score"] = scores[server_id][winnnerDisplay].get("score", 0) + 1
        scores[server_id][loserDisplay]["score"] = scores[server_id][loserDisplay].get("score", 0) - 1
        scores[server_id][winnnerDisplay]["wins"] = scores[server_id][winnnerDisplay].get("wins", 0) + 1
        scores[server_id][loserDisplay]["losses"] = scores[server_id][loserDisplay].get("losses", 0) + 1

        # Save scores to file
        with open('scores.json', 'w') as f:
            json.dump(scores, f)

        # Get the current scores, wins, and losses of the winner and loser
        winnerScore = scores[server_id][winnnerDisplay]["score"]
        loserScore = scores[server_id][loserDisplay]["score"]
        winnerWins = scores[server_id][winnnerDisplay]["wins"]
        loserLosses = scores[server_id][loserDisplay]["losses"]

        return f"{ctx.author.mention} rolled {authorRoll}, {opponent} rolled {opponentRoll}. {winner} wins. Score: {winnerScore}  {loser} score: {loserScore}"
    else:
        return "You must mention a user to start a battle."
    
# Update get_scores function
def get_scores(ctx):
    server_id = str(ctx.guild.id)
    if server_id not in scores:
        return "No scores yet!"
    return "\n".join([f"{user}: Score - {data['score']}, Wins - {data['wins']}, Losses - {data['losses']}" for user, data in scores[server_id].items()])
