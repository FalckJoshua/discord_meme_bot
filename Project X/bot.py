from typing import Final
from discord import Intents, Client, Message
import os
from dotenv import load_dotenv
from responses import get_response, play
from discord.ext import commands


load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
print(TOKEN)

intents: Intents = Intents.default()
intents.message_content = True  # NOQA
bot: commands.Bot = commands.Bot(command_prefix="$", intents=intents)

async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print("Message is empty")
        return
    is_private = False
    if user_message[0] == '$':
        is_private = True
        user_message = user_message[1:]
    elif user_message[0] == '%':
        user_message = user_message[1:]
    else:
        return
    try:
        ctx = await bot.get_context(message)
        response: str = await get_response(ctx, user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(f"Error: {e}")

@bot.event
async def on_ready() -> None:
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message: Message) -> None:
    if message.author == bot.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    
    print(f'{username} said {user_message} in {channel}')
    
    await send_message(message, user_message)

def main() -> None:
    bot.run(TOKEN)

if __name__ == '__main__':
    main()