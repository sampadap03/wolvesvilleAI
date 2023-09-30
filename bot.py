from discord.ext.commands import Bot as bot
import discord
import responses
import json

async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def get_token():
    with open('config.json', 'r') as myfile:
        data=myfile.read()
    
    return json.loads(data)["TOKEN"]


async def run_discord_bot():
    token = get_token()

    discord.utils.setup_logging()
    intents = discord.Intents.default()
    intents.message_content = True

    client = bot(command_prefix=".", intents=intents)


    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    async with client:
        await client.load_extension("cogs.common")
        await client.load_extension("cogs.clan")
       
        await client.start(token)
