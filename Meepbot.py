#BOT
import discord
from discord.ext import commands
from discord.ext.commands import Bot


import asyncio
import itertools
import random
import io



bot = commands.Bot(command_prefix='.')
bot.remove_command('help')


@bot.event
async def on_ready():
    print ("Ready when you are XD")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name='.help'))


@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: pong!")
    print ("user has pinged")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("The users name is: {}".format(user.name))
    await bot.say("The users ID is: {}".format(user.id))
    await bot.say("The users status is: {}".format(user.status))
    await bot.say("The users highest role is: {}".format(user.top_role))
    await bot.say("The user joined at: {}".format(user.joined_at))
    print ("info has been given")

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Cya, {}. Ya loser!".format(user.name))
    await bot.kick(user)
    print ("member has been kicked")


@bot.command(pass_text=True)
async def snazz(message: str=None):
    if message is None:
        p = random.choice([":yellow_heart: You're perfect the way you are, Babe",
                            "YOU'RE A CRAZY CAT GIRL AND I LOVE THAT!",
                            "Smile for me!",
                            "Thanks for always being there for me <3",
                            "https://giphy.com/gifs/thanks-thank-you-kazoo-kid-l3q2wJsC23ikJg9xe",
                            "You're wonderful :yellow_heart:",
                            "https://giphy.com/gifs/UCZ88v3wSZFHW",
                            "https://giphy.com/gifs/love-art-cute-l4pTdcifPZLpDjL1e",
                            "https://www.youtube.com/watch?v=XDwPk7lMOps",
                            "https://www.youtube.com/watch?v=IPhPkxxxOKk"])
        await bot.say(p)

@bot.command(pass_context=True)
async def meep(ctx):
    await bot.say("https://media.giphy.com/media/qQISII17mATiE/giphy.gif") 

@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author 

    embed = discord.Embed(
        colour = discord.Colour.green()
    )
    embed.set_author(name='Help')
    embed.add_field(name='.ping', value='Returns pong', inline=False)
    embed.add_field(name='.info @member', value='Gives you information about the member', inline=False)
    embed.add_field(name='.kick @member', value='Kicks the member', inline=False)
    embed.add_field(name='.greet', value='AYO', inline=False)
    embed.add_field(name='.snazz', value='Love you Snazz <33', inline=False)
    embed.add_field(name='.meep', value='Because why not', inline=False)
    embed.add_field(name='invite', value='Gives you the invite link for this bot', inline=False)
    embed.add_field(name='!help', value='Gives you the music commands', inline=False)
    embed.add_field(name='.bubbles', value='BUBBLES', inline=False)
    embed.add_field(name='.shower', value='you stink', inline=False)
    embed.add_field(name='.nice @member', value='show your friend how nice they are', inline=False)
    embed.add_field(name='.mom @member', value='Burn', inline=False)
    embed.add_field(name='.bedtime @member', value='Goodnight', inline=False)
    embed.add_field(name='.meach', value='lol', inline=False)
    embed.add_field(name='.bye', value='bye', inline=False)
    embed.add_field(name='.tea', value='ew', inline=False)
    embed.add_field(name='.Lenny', value='Lenny ILY', inline=False)
    embed.add_field(name='.pocker', value='Eh you know...', inline=False)
    embed.add_field(name='.gi', value='Too cool for school', inline=False)
    embed.add_field(name='.cat', value='You gotta love cats', inline=False)

    await bot.send_message(author, embed=embed)
    await bot.say("A DM has been sent to you!")

@bot.command(pass_context=True)
async def msg(ctx, message: str=None):
    author = ctx.message.author
    if message is None:
        c = random.choice(["Hello!",
                           "What's up!",
                           "How's your day? :3",
                           "Just sliding into your DMs :sunglasses:",
                           "Nice to meet you!",
                           "I hope your day is wonderful!",
                           "Thank you for inviting me to your DMs! I'm sure we'll have lots of fun together :3",
                           "Can I tell you a secret? Martin is actually a terrible owner",
                           "Whale hello there! Nice to sea you :D",
                           "BEST FRIENDS FOREVER!",
                           "Tell Martin he's a loser",
                           "HAI!!!!!!!",
                           "https://www.youtube.com/watch?v=ZaeCvdZtsgo",
                           "https://www.youtube.com/watch?v=B7bqAsxee4I",
                           "https://www.youtube.com/watch?v=fFnsqVEMIbs",
                           "https://www.youtube.com/watch?v=EcXURC_nNhc",
                           "A day without sunshine is like night",
                           "Have you ever been running and accidentally ran into a parked car and fell down and said, 'I like cheesecake?' Me neither.",
                           "Quick, what's the number for 911?!",
                           "Just because I'm stupid doesn't mean I'm dumb"])
    await bot.send_message(author, c)
    await bot.say("CHECK YOUR DMs!!!!!!!")

@bot.command(pass_text=True)
async def pun(message: str=None):
    if message is None:
        t = random.choice(["What do you call a fake noodle? An Impasta.",
                           "I would avoid the sushi if I was you. It’s a little fishy.",
                           "Want to hear a joke about paper? Nevermind it’s tearable.",
                           "Why did the cookie cry? Because his father was a wafer so long!",
                           "I used to work in a shoe recycling shop. It was sole destroying.",
                           "What do you call a belt with a watch on it? A waist of time.",
                           "How do you organize an outer space party? You planet.",
                           "I went to a seafood disco last week... and pulled a mussel.",
                           "Do you know where you can get chicken broth in bulk? The stock market.",
                           "I cut my finger chopping cheese, but I think that I may have greater problems.",
                           "My cat was just sick on the carpet, I don’t think it’s feline well.",
                           "Why did the octopus beat the shark in a fight? Because it was well armed.",
                           "How much does a hipster weigh? An instagram.",
                           "What did daddy spider say to baby spider? You spend too much time on the web.",
                           "Atheism is a non-prophet organisation.",
                           "There’s a new type of broom out, it’s sweeping the nation.",
                           "What cheese can never be yours? Nacho cheese.",
                           "What did the Buffalo say to his little boy when he dropped him off at school? Bison.",
                           "Have you ever heard of a music group called Cellophane? They mostly wrap.",
                           "Why does Superman gets invited to dinners? Because he is a Supperhero.",
                           "How was Rome split in two? With a pair of Ceasars.",
                           "The shovel was a ground breaking invention.",
                           "A scarecrow says, 'This job isn't for everyone, but hay, it's in my jeans.'",
                           "A Buddhist walks up to a hot dog stand and says, 'Make me one with everything.'",
                           "Did you hear about the guy who lost the left side of his body? He's alright now.",
                           "What do you call a girl with one leg that's shorter than the other? Ilene.",
                           "I did a theatrical performance on puns. It was a play on words.",
                           "What do you do with a dead chemist? You barium.",
                           "I bet the person who created the door knocker won a Nobel prize.",
                           "Towels can’t tell jokes. They have a dry sense of humor.",
                           "Two birds are sitting on a perch and one says 'Do you smell fish?'",
                           "Do you know sign language? You should learn it, it’s pretty handy.",
                           "What do you call a beautiful pumpkin? GOURDgeous.",
                           "Why did one banana spy on the other? Because she was appealing.",
                           "What do you call a cow with no legs? Ground beef.",
                           "What do you call a cow with two legs? Lean beef.",
                           "What do you call a cow with all of its legs? High steaks.",
                           "A cross eyed teacher couldn’t control his pupils.",
                           "After the accident, the juggler didn’t have the balls to do it.",
                           "I used to be afraid of hurdles, but I got over it.",
                           "To write with a broken pencil is pointless."])
        await bot.say(t)


@bot.command(pass_context=True)
async def invite(ctx):
    await bot.say("https://discordapp.com/oauth2/authorize?client_id=457850680913166336&scope=bot")

@bot.command(pass_context=True)
async def bubbles(ctx):
    await bot.say("https://giphy.com/gifs/sesame-street-muppets-elmo-l4HogOSqU3uupmvmg")    

@bot.command(pass_context=True)
async def shower(ctx):
    await bot.say("https://giphy.com/gifs/season-4-the-simpsons-4x3-3o6MbjjOqVPMHZvuve")

@bot.command(pass_context=True)
async def nice(ctx, user: discord.Member):
    await bot.say("You're a nice human being {}. ILY!".format(user.name))

@bot.command(pass_context=True)
async def mom(ctx, user: discord.Member):
    await bot.say("Your mom told me you're her biggest regret, {}. She's good in bed though".format(user.name))

@bot.command(pass_context=True)
async def bedtime(ctx, user: discord.Member):

  await bot.say("Mom duck had two little ducklings. Every day mom duck took her ducklings to the river. She said to them, “Babies, stay near me. Do not go far from me. If you go far, the fox will eat you up.” Every day the fox saw the ducklings. He wanted to eat them. But mom duck was big and strong. The fox was afraid of her. One day mom duck and the ducklings went to the river. The fox was hungry. He said, “Today Ill eat the ducklings.” The fox too went to the river. He hid behind a bush. He thought, “When mom duck goes away, Ill eat the ducklings.” They had a jolly time in the river. Then they said, “Mom were hungry. We want some frogs” Mom duck said, “Ill go and catch some frogs. Wait here. Do not go out of the water, or the foxll catch you.” “Ok, mom,” said the ducklings. Mom duck went out to catch frogs. The fox saw her go. “The ducklings are all alone,” he said. “Now Ill eat them.” The fox wanted to catch them, but he didnt like to go into the water. The fox said, “Babies, come here. Ill give you frogs to eat.” The ducklings said, “Mom told us not to come out of the water. So well stay here.” The fox was angry. Then he saw a log of wood in the river. “Oh, Ill jump on the log,” he said to himself. -when the log goes near the ducklings, Ill catch them.” The fox jumped on the log. The log floated down the river. but it did not go near the ducklings. It took the fox far, far away. The ducklings were safe. When mother duck came back the ducklings said, “Mom, the fox wanted to catch us. He called us. But we did not get out of the water. He jumped on a log to catch us. But the log took him far down the river.” Mother duck was happy. She said, “I am glad the bad fox is gone. Hell not come now. ” “Quack-quack!” said the ducklings. They ate and were very happy... Goodnight, {} :sleeping:".format(user.name))

@bot.command(pass_context=True)
async def meach(ctx):
    await bot.say("https://media.giphy.com/media/kFgzrTt798d2w/giphy.gif")

@bot.command(pass_context=True)
async def bye(ctx):
    await bot.say("https://giphy.com/gifs/K0dM34TGaMkcE")

@bot.command(pass_context=True)
async def tea(ctx):
    await bot.say("https://giphy.com/gifs/desusandmero-viceland-desus-mero-l0HlwwRxfcVEr4AUg")

@bot.command(pass_text=True)
async def Lenny(message: str=None):
    if message is None:
        z = random.choice(["https://giphy.com/gifs/lenny-5uZjTWWr8gK8U",
                           "https://giphy.com/gifs/disney-hello-hey-fOtA9hO1bNmaQ",
                           "https://giphy.com/gifs/day-reddit-posts-X3FmqQ7ehoCBy",
                           "Love you, Boobers!",
                           "Tiny carrot :heart: you",
                           "Thank you for teaching me how to cook pasta",
                           "You mean a lot to me",
                           "https://giphy.com/gifs/french-Wciz7eToYvIZ2",
                           "https://www.youtube.com/watch?v=L0MK7qz13bU"])
        await bot.say(z)

@bot.command(pass_text=True)
async def pocker(message: str=None):
    if message is None:
        i = random.choice(["https://giphy.com/gifs/not-a-single-fuck-was-given-game-show-o0mMd3mpQApzy",
                           "https://giphy.com/gifs/burgerrecords-burger-records-todays-hits-xT8qBvOmIEWXxVPdxS",
                           "https://giphy.com/gifs/acttIrNAHaoco",
                           "https://giphy.com/gifs/realitytvgifs-real-housewives-realitytvgifs-tqcEVtTVNIA2A",
                           "https://giphy.com/gifs/christmas-father-scottish-k2OvswmOVsEec",
                           "https://giphy.com/gifs/tommy-sheridan-socialist-m596iSjfwVfnq"])
        await bot.say(i)

@bot.command(pass_text=True)
async def test(message: str=None):
    if message is None:
        w = random.choice(['<iframe src="https://giphy.com/embed/oAyH7AS1tB3J6" width="480" height="314" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/family-guy-peter-griffin-oAyH7AS1tB3J6">via GIPHY</a></p>'])
    await bot.say(w)

@bot.command(pass_text=True)
async def gi():
    await bot.say("https://imgur.com/a/bOTqw6j")

@bot.command(pass_text=True)
async def cat(message: str=None):
    if message is None:
        t = random.choice(["https://giphy.com/gifs/cat-33OrjzUFwkwEg",
                           "https://giphy.com/gifs/JIX9t2j0ZTN9S",
                           "https://giphy.com/gifs/cat-hello-oh-MWSRkVoNaC30A",
                           "https://giphy.com/gifs/cat-sea-chicks-12PA1eI8FBqEBa",
                           "https://giphy.com/gifs/cat-moment-remember-8vQSQ3cNXuDGo",
                           "https://giphy.com/gifs/transparent-baby-shake-nNxT5qXR02FOM",
                           "https://giphy.com/gifs/justin-cat-trippy-psychedelic-26FPCXdkvDbKBbgOI",
                           "https://giphy.com/gifs/room-E0cyxhawhe9dm",
                           "https://giphy.com/gifs/funny-cat-mlvseq9yvZhba",
                           "https://giphy.com/gifs/cat-kisses-hugs-MDJ9IbxxvDUQM",
                           "https://giphy.com/gifs/cat-trip-tripping-l0MYNB04rBb51QNtC",
                           "https://giphy.com/gifs/animals-being-jerks-dicks-yltHqiCQ2b5pm",
                           "https://giphy.com/gifs/animals-being-dicks-10APf3POAhlI1G",
                           "https://giphy.com/gifs/cheezburger-cat-mountain-good-job-fXgKfzV4aaHQI",
                           "https://giphy.com/gifs/jerseydemic-3oriO0OEd9QIDdllqo",
                           "https://giphy.com/gifs/reaction-Nm8ZPAGOwZUQM",
                           "https://giphy.com/gifs/cat-waterfall-wet-B7ppUExX92PjW",
                           "https://giphy.com/gifs/aww-11s7Ke7jcNxCHS",
                           "https://giphy.com/gifs/cat-weird-bra-p4xp4BjHIdane",
                           "https://giphy.com/gifs/cat-money-cash-ND6xkVPaj8tHO"
                           ])
        await bot.say(t)

@bot.command(pass_text=True)
async def greet(message: str=None):
    if message is None:
        q = random.choice([":yum: :wave: AYO!",
                           "Heyy!!!",
                           ":wave: What's up!",
                           "Sup :sunglasses:",
                           "Hej med dig :3",
                           "Hey! How are you? :yum:",
                           "Greetings :vulcan:"])                
        await bot.say(q)

@bot.command(pass_text=True)
async def em(message: str=None):
    if message is None:
        b = random.choice(["https://giphy.com/gifs/minecraft-BljlTfIli47x6",
                            "EM, YOU'RE SO FREAKING NICE AND I'M SO HAPPY YOU'RE MY FRIEND!",
                            "Manchester",
                            "https://imgur.com/a/gNn1lxk",
                            "https://giphy.com/gifs/ladylamb-mom-pop-music-bayonne-l0HFi4SqqafGmMyFG",
                            "Em-in-Em",
                            "https://www.youtube.com/watch?v=_Yhyp-_hX2s",
                            ""])
        await bot.say(b)


@bot.event
async def on_message(message):
    if "moop" in message.content:
         await bot.send_message(message.channel, "It's Mr. Moop to you, sir!")

    if "smh" in message.content:
         await bot.send_message(message.channel, "Don't shake your head too much")
    
    if "truck" in message.content:
        await bot.send_message(message.channel, "DID SOMEONE SAY TRUCK!?!?!??")
    
    if "bw" in message.content:
        await bot.send_message(message.channel, "Nobody wanna play BW with **you** ")
    
    if "Hello" in message.content:
        await bot.send_message(message.channel, "Hey!")

    
    if "swedish" in message.content:
         await bot.send_message(message.channel, "Don't mention anything that has to do with Sweden around me!")
    await bot.process_commands(message)
    
    

    

bot.run("NDU3ODUwNjgwOTEzMTY2MzM2.Di6Y6Q.oNmCbJ99fh_1_XSIegw7yhPq6lk")  