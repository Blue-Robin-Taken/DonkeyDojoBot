import discord
import os
import json

intents = discord.Intents.all()
bot = discord.Bot(intents=intents)


@bot.event
async def on_connect():
    print(f"Bot has connected as: {bot.user}")

    # -- Setup Cogs --
    with open(os.path.abspath("./config.json"), "r") as setup_json:  # Use the setup folder to get the cogs folder
        cogs_folder = json.load(setup_json)["cogs_folder"]  # Load cogs folder from setup JSON

    with open(os.path.abspath(cogs_folder + "/cogs.json"), "r") as cogs_setup_json:
        cogs_json = json.load(cogs_setup_json)  # Json for the list of cogs

    for sub_folder in cogs_json["sub_folders"]:
        for file in cogs_json["sub_folders"][sub_folder]["files"]:
            print(file)
            file_path = f"{cogs_folder.replace('/', '').replace('.', '')}.{sub_folder}.{file}"
            print(f"Loaded {file_path}")
            bot.load_extension(file_path)

    await bot.sync_commands()


@bot.event
async def on_ready():
    print("Bot is ready!")


@bot.slash_command(name='ping')
async def ping(ctx):
    await ctx.respond(f"Pong! Bot latency: {bot.latency * 1000}ms")


bot.run(str(os.getenv('TOKEN')))
