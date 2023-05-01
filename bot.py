# Import required modules.
import discord
import random
import asyncio
import pymongo

# Import packages from modules.
from discord.ext import commands
from pymongo import MongoClient
from pymongo.server_api import ServerApi

''' ------------------------------------------------------------------------------------------------------------------------------------------------ '''
# Bot and Database setup. 

bot = commands.Bot(command_prefix='.', intents = discord.Intents.all())

TOKEN  = 

uri = 

client = MongoClient(uri, server_api=ServerApi('1'))

db = client["HouseCup"]

players_collection = db["Players"]

bot.help_command = None
''' ------------------------------------------------------------------------------------------------------------------------------------------------ '''
# Declare Dictionaries

harry_potter_qa = {
    "What was the name of Harry's owl?": "Hedwig",
    "What position does Harry play in Quidditch?": "Seeker",
    "What is the name of the train that takes Hogwarts students to school?": "Hogwarts Express",
    "What are the names of Harry's parents?": "James and Lily Potter",
    "Who is the headmaster of Hogwarts School of Witchcraft and Wizardry?": "Albus Dumbledore",
    "What is the name of the three-headed dog that guards the Philosopher's Stone?": "Fluffy",
    "Who is Ron Weasley's best friend?": "Harry Potter",
    "What is the name of the snake that Voldemort uses as a horcrux?": "Nagini",
    "What is the name of the ghost who haunts the girls' bathroom at Hogwarts?": "Moaning Myrtle",
    "What is the name of the Weasley family's home?": "The Burrow",
    "What is the name of Hermione's cat?": "Crookshanks",
    "What is the name of the wizard prison guarded by Dementors?": "Azkaban",
    "What is the name of the creature that sucks the happiness out of people?": "Dementor",
    "What is the name of the wizarding village near Hogwarts?": "Hogsmeade",
    "What is the name of the plant that Neville Longbottom is particularly good at growing?": "Mimbulus Mimbletonia",
    "Who is the author of the Harry Potter books?": "J.K. Rowling",
    "What is the name of the gamekeeper at Hogwarts?": "Rubeus Hagrid",
    "What is the name of the wizarding school in America?": "Ilvermorny",
    "What is the name of the dragon that Hagrid hatches in the first book?": "Norbert",
    "What is the name of the pub in Hogsmeade that serves butterbeer?": "The Three Broomsticks",
    "What is the name of the plant that Mandrakes evolve into?": "Mandragora",
    "What is the name of the wandmaker in Diagon Alley?": "Ollivander",
    "What is the name of the centaur who teaches Divination at Hogwarts?": "Firenze",
    "What is the name of the head of the Department of Magical Law Enforcement?": "Pius Thicknesse",
    "What is the name of the spell that causes objects to multiply?": "Geminio",
    "What is the name of the elf who serves the Malfoy family?": "Dobby",
    "What is the name of the House-Elf who belonged to the Black family?": "Kreacher",
    "What is the name of the wizard who invented the Sorcerer's Stone?": "Nicolas Flamel",
    "What is the name of the potion that causes the drinker to fall in love?": "Amortentia",
    "What is the name of the sport played on broomsticks in the Harry Potter books?": "Quidditch",
    "What is the name of the spell that creates a Patronus?": "Expecto Patronum",
    "What is the name of the house that Harry, Ron, and Hermione are in at Hogwarts?": "Gryffindor",
    "What is the name of the game that Hermione creates to fight against Voldemort's Death Eaters?": "Dumbledore's Army",
    "What is the name of the house-elf who belonged to the Lovegood family?": "Dobby",
    "What is the name of the magical object that allows the user to travel back in time?": "Time-Turner",
    "What is the name of the potion that grants the drinker luck?": "Liquid Luck" or "Felix Felicis",
    "What is the name of the dragon that guards the vaults at Gringotts Bank?": "Ukranian Ironbelly",
    "What is the name of the wizard who killed Harry's parents?": "Voldemort" or "Tom Riddle",
    "What is the name of the house-elf who helps Harry, Ron, and Hermione break into Gringotts Bank?": "Griphook",
    "What is the name of the werewolf who teaches Defense Against the Dark Arts at Hogwarts in Harry's third year?": "Remus Lupin",
    "What is the name of the spell that creates a fiery 'rope' that can be used to bind and control someone?": "Incarcerous",
    "What is the name of the creature that is attracted to shiny objects and is known for hoarding treasure?": "Niffler"
}

''' ------------------------------------------------------------------------------------------------------------------------------------------------ '''
# Help Command

@bot.command()
async def help(ctx):
    # Create two separate embeds for each page
    embed = discord.Embed(title="Commands List - Page 1 of 2", description="[Click Me!](https://top.gg/servers/1095101909016260769) To join our support server!", color=ctx.author.color)
    embed.add_field(name=".setup", value="Creates roles needed for usage.", inline=False)
    embed.add_field(name=".enrol", value="Allows a user to select their house.", inline=False)
    embed.add_field(name=".question", value="Generates a question for the user to answer.", inline=False)
    embed.add_field(name=".houselb", value="Shows the current global leaderboard!", inline=False)

    await ctx.reply(embed=embed)
    

''' ------------------------------------------------------------------------------------------------------------------------------------------------ '''
# Role Selection & Creation.

@bot.command()
@commands.has_permissions(manage_roles=True)
async def setup(ctx):

    # Create roles
    guild = ctx.guild
    roles = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    created_roles = []

    for role_name in roles:
        created_role = await guild.create_role(name=role_name)
        created_roles.append(created_role)

    # Send confirmation message
    role_names = ", ".join(role.mention for role in created_roles)
    await ctx.send(f"The following roles have been created: {role_names}")

@bot.command()
async def enrol(ctx):
     
    # Create roles embed.
    embed = discord.Embed(
    title=f"{ctx.author.name} Please select your house by reacting below! Remember you cannot change your house after you join, so choose carefully 🧙‍♂️", 
    description = "React to enrol into a house!", 
    color = ctx.author.color)
    embed.add_field(name="Gryffindor", value="🦁", inline=False)
    embed.add_field(name="Hufflepuff", value="🦡", inline=False)
    embed.add_field(name="Ravenclaw", value="🦅", inline=False)
    embed.add_field(name="Slytherin", value="🐍", inline=False)
     
     # Send roles embed and name the variable for it.
    enrol_embed = await ctx.send(embed=embed)

      # Add reactions to the embed.
    await enrol_embed.add_reaction("🦁")
    await enrol_embed.add_reaction("🦡")
    await enrol_embed.add_reaction("🦅")
    await enrol_embed.add_reaction("🐍")

    # Function to check if the reaction is valid.
    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["🦁", "🦡", "🦅", "🐍"]

    try:
        reaction, user = await bot.wait_for("reaction_add", timeout=60, check=check)
    except asyncio.TimeoutError:
        await ctx.send("You took too long to respond! Try again.")
        return

    # Assign the role based on the reaction.

    # Gryffindor
    if str(reaction.emoji) == "🦁":
        role = discord.utils.get(ctx.guild.roles, name="Gryffindor")
        await ctx.author.add_roles(role)

        embed = discord.Embed(
        title=f"{ctx.author.name} Welcome to Gryffindor!",
        description="Gryffindor house is where you would find the pluckiest and most daring students (there’s a reason the house symbol is the brave lion). \n\n The house colours are scarlet and gold and the common room lies up in Gryffindor Tower. \n\n Some of the wizarding world’s best and brightest belonged to this house – Harry Potter and Albus Dumbledore are just a couple that spring to mind! \n\n If you are lucky enough to end up in Gryffindor, we imagine you’re the type of person who likes to stand up for the little guy, challenges authority, has a tendency to act first and think later, is known as a class clown and takes board games very seriously.",
        color = discord.Color.red())
        embed.set_image(url="https://cdn.discordapp.com/attachments/957641774694797332/1102308875014783006/pngaaa.com-2050957.png")

        await ctx.send(embed=embed)

    # Hufflepuff
    elif str(reaction.emoji) == "🦡":
        role = discord.utils.get(ctx.guild.roles, name="Hufflepuff")
        await ctx.author.add_roles(role)

        embed = discord.Embed(
        title=f"{ctx.author.name} Welcome to Hufflepuff!",
        description="Hufflepuff is where you will find the most trustworthy and hardworking students. In fact, out of all the houses Hufflepuff has produced the least number of dark witches and wizards. The badger is the symbol of this house, the colours are yellow and black and the common room can be found near the kitchens in Hogwarts. \n\n There is an idea that Hufflepuffs are the least clever of all Hogwarts students – but that is not true. Hufflepuffs are just the most humble of all the houses and don’t feel the need to shout about their achievements in the same way as the others. \n\n If you were lucky enough to be sorted into this house, we can imagine you’re the type of person who has a strong moral compass, always works hard, is the most loyal friend, knows it is the taking part that counts and always has the best snacks.",
        color = discord.Color.yellow())

        embed.set_image(url="https://cdn.discordapp.com/attachments/957641774694797332/1102309186357956730/pngaaa.com-1203607_2.png")

        await ctx.send(embed=embed)
         
    # Ravenclaw
    elif str(reaction.emoji) == "🦅":
        role = discord.utils.get(ctx.guild.roles, name="Ravenclaw")
        await ctx.author.add_roles(role)

        embed = discord.Embed(
        title=f"{ctx.author.name} Welcome to Ravenclaw!",
        description="f you are looking for the brainiest students – you would find them in Ravenclaw (with a couple of notable exceptions like Hermione Granger). The Ravenclaw colours are blue and bronze, the emblem is an eagle and the common room sits at the top of Ravenclaw Tower behind an enchanted knocker. \n\n The Sorting Hat would only put you in this house if you demonstrated excellent wisdom, wit and a skill for learning. Ravenclaws are often known for being quite eccentric and most of the great wizarding inventors and innovators have come from this house. \n\n We can imagine that you would get to sit up in Ravenclaw Tower, while surveying the excellent views, if you’re the type of person who analyses everything, is an overachiever, can be described as away with the fairies, is not afraid to be an individual and has a head stuffed full of interesting facts.",
        color = discord.Color.blue())

        embed.set_image(url="https://cdn.discordapp.com/attachments/957641774694797332/1102308874721177705/pngaaa.com-2050932.png")

        await ctx.send(embed=embed)

    # Slytherin 
    elif str(reaction.emoji) == "🐍":
        role = discord.utils.get(ctx.guild.roles, name="Slytherin")
        await ctx.author.add_roles(role)

        embed = discord.Embed(
        title=f"{ctx.author.name} Welcome to Slytherin!",
        description="Slytherin house has an unfortunate reputation. While it is true that a lot of dark witches and wizards were sorted into Slytherin, not all who belong to this house are bad. In fact, there are a lot of excellent qualities the Sorting Hat looks for in potential Slytherins and Merlin himself even belonged to this misunderstood house! \n\n The house colours for Slytherin are silver and emerald green and the emblem is a serpent. The common room can be found down in the dungeons under the lake (which only adds to the Slytherin air of mystery). \n\n If the Sorting Hat placed you in this noble house, then you are most likely ambitious, shrewd and possibly destined for greatness. We can imagine you’re the kind of person who is always one step ahead, has a dark sense of humour, thinks reputation is important, takes pride in their appearance and doesn’t let anyone see their soft side.",
        color = discord.Color.green())
         
        embed.set_image(url="https://cdn.discordapp.com/attachments/957641774694797332/1102308873794240583/pngaaa.com-4381667.png")

        await ctx.send(embed=embed)

''' ------------------------------------------------------------------------------------------------------------------------------------------------ '''
# Quiz Logic

@bot.command()
async def question(ctx):
    question = random.choice(list(harry_potter_qa.keys()))

    question_embed = discord.Embed(
        title=f"{ctx.author.name} - Here is your question:",
        description=f"{question}",
        color=ctx.author.color)
    await ctx.send(embed=question_embed)

    response = await bot.wait_for('message', check=lambda message: message.author == ctx.author and message.content.lower())

    member = ctx.guild.get_member(ctx.author.id)
    for role in member.roles:
        if role.name == 'Gryffindor':
            house = 'Gryffindor'
            if response.content.lower() == harry_potter_qa[question].lower():
           
                players_collection.update_one({"_id": str(ctx.author.id)}, {"$inc": {f"points.{house}": 1}}, upsert=True)
                await ctx.send(f"Congratulations {ctx.author.name}, you have earned 1 point for {house}!")

            else:
                await ctx.send(f"Sorry, that's not the correct answer. Try another question! Answer: {harry_potter_qa[question]}")

        elif role.name == 'Slytherin':
            house = 'Slytherin'

            if response.content.lower() == harry_potter_qa[question].lower():
           
                players_collection.update_one({"_id": str(ctx.author.id)}, {"$inc": {f"points.{house}": 1}}, upsert=True)
                await ctx.send(f"Congratulations {ctx.author.name}, you have earned 1 point for {house}!")
            
            else:
                await ctx.send(f"Sorry, that's not the correct answer. Try another question! Answer: {harry_potter_qa[question]}")

        elif role.name == 'Hufflepuff':
            house = 'Hufflepuff'#

            if response.content.lower() == harry_potter_qa[question].lower():
           
                players_collection.update_one({"_id": str(ctx.author.id)}, {"$inc": {f"points.{house}": 1}}, upsert=True)
                await ctx.send(f"Congratulations {ctx.author.name}, you have earned 1 point for {house}!")
            
            else:
                await ctx.send(f"Sorry, that's not the correct answer. Try another question! Answer: {harry_potter_qa[question]}")

        elif role.name == 'Ravenclaw':
            house = 'Ravenclaw'

            if response.content.lower() == harry_potter_qa[question].lower():
           
                players_collection.update_one({"_id": str(ctx.author.id)}, {"$inc": {f"points.{house}": 1}}, upsert=True)
                await ctx.send(f"Congratulations {ctx.author.name}, you have earned 1 point for {house}!")
            
            else:
                await ctx.send(f"Sorry, that's not the correct answer. Try another question! Answer: {harry_potter_qa[question]}")

        else:
            house = None

''' ------------------------------------------------------------------------------------------------------------------------------------------------ '''
# Leaderboard Command

@bot.command()
async def houselb(ctx):
    # Query MongoDB for total points for each house
    results = players_collection.aggregate([
        {
            "$group": {
                "_id": None,
                "Gryffindor": {"$sum": "$points.Gryffindor"},
                "Slytherin": {"$sum": "$points.Slytherin"},
                "Hufflepuff": {"$sum": "$points.Hufflepuff"},
                "Ravenclaw": {"$sum": "$points.Ravenclaw"}
            }
        }
    ])

    # Format results as an embed
    leaderboard_embed = discord.Embed(title="House Cup Leaderboard", color=0xffd700)

    for result in results:
        gryffindor_points = result['Gryffindor']
        slytherin_points = result['Slytherin']
        hufflepuff_points = result['Hufflepuff']
        ravenclaw_points = result['Ravenclaw']
        total_points = gryffindor_points + slytherin_points + hufflepuff_points + ravenclaw_points

        leaderboard_embed.add_field(
            name=f"Current Points",
            value=f"🦁 Gryffindor: {gryffindor_points}\n 🐍 Slytherin: {slytherin_points}\n 🦡 Hufflepuff: {hufflepuff_points}\n 🦅 Ravenclaw: {ravenclaw_points}",
            inline=False
        )

    await ctx.send(embed=leaderboard_embed)

''' ------------------------------------------------------------------------------------------------------------------------------------------------ '''
# Run Scripts & Tests

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.event
async def on_ready():
    print("Bot is ready for action!")

bot.run(TOKEN)