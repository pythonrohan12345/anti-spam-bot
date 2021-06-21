from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print("Anti spam bot on its duty!")
    while True:
        print("cleared")
        await asyncio.sleep(10)
        with open("spam_detect.txt", "r+") as file:
            file.truncate(0)

@bot.event
async def on_message(message):
    counter = 0
    with open("spam_detect.txt", "r+") as file:
        for lines in file:
            if lines.strip("\n") == str(message.author.id):
                counter += 1
            
        file.writelines(f"{str(message.author.id)}\n")
        if counter > 5:
                await message.guild.ban(message.author, reason="spam")
                await asyncio.sleep(1)
                await message.guild.unban(message.author)
                print(f"Uh {message.author} was spamming and were kicked from the server.")

bot.run("ODE0OTA0ODE0Mzc4NDE4MTk3.YDkpPw.CFu7Uit4nD2vCf-u64qnfn0YI9U")