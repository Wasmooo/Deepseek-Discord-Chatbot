import os
import discord
import requests
import json
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_BOT_TOKEN')
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
ADMIN_USER_IDS = [12345678910,]  # add user id's of admins here. separate with commas (they can change personalities)

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"
PERSONALITY_FILE = "user_personalities.json"

DEFAULT_PERSONALITY = ()  # put the default personality here (double quotes before and after)

# Load stored personalities
def load_personalities():
    if os.path.exists(PERSONALITY_FILE):
        try:
            with open(PERSONALITY_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error: The personalities file is invalid or empty. Creating a new one.")
            return {}
    return {}

# Save personalities to file
def save_personalities():
    with open(PERSONALITY_FILE, "w") as file:
        json.dump(user_personalities, file, indent=4)

user_personalities = load_personalities()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await bot.tree.sync()

@bot.tree.command(name="setpersonality", description="Set a personality for a specific user (admin only).")
async def set_personality(interaction: discord.Interaction, user: discord.Member, personality: str):
    """Admin command to assign a personality to a user."""
    if interaction.user.id in ADMIN_USER_IDS:  # check if user is an admin
        user_id = str(user.id)
        user_personalities[user_id] = personality
        save_personalities()
        await interaction.response.send_message(f"Personality for {user.display_name} has been updated.")
    else:
        await interaction.response.send_message("You don't have permission to set personalities.", ephemeral=True)

@bot.tree.command(name="removepersonality", description="Remove a user's custom personality (admin only).")
async def remove_personality(interaction: discord.Interaction, user: discord.Member):
    """Admin command to remove a user's assigned personality."""
    if interaction.user.id in ADMIN_USER_IDS:  
        user_id = str(user.id)
        if user_id in user_personalities:
            del user_personalities[user_id]  
            save_personalities()  
            await interaction.response.send_message(f"Removed {user.display_name}'s custom personality.")
        else:
            await interaction.response.send_message(f"{user.display_name} doesn't have a custom personality set.", ephemeral=True)
    else:
        await interaction.response.send_message("You don't have permission to remove personalities.", ephemeral=True)


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if bot.user.mentioned_in(message):
        user_message = message.content.replace(f'<@{bot.user.id}>', '').strip()
        user_id = str(message.author.id)

        # combine  personality with user's custom one
        custom_personality = user_personalities.get(user_id, "")
        full_personality = f"{DEFAULT_PERSONALITY} {custom_personality}".strip()

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
        }
        data = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": full_personality},
                {"role": "user", "content": user_message}
            ]
        }

        response = requests.post(DEEPSEEK_API_URL, headers=headers, json=data)

        if response.status_code == 200:
            result = response.json()
            reply = result.get("choices", [{}])[0].get("message", {}).get("content", "I couldn't generate a response.")
        else:
            reply = f"Error: {response.status_code} - Unable to contact DeepSeek API."

        await message.reply(reply)

    await bot.process_commands(message)

bot.run(TOKEN)
