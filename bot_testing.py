import discord
import random
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix='.')

cat_pics = [
    'https://img.webmd.com/dtmcms/live/webmd/consumer_assets/site_images/article_thumbnails/other/cat_relaxing_on_patio_other/1800x1200_cat_relaxing_on_patio_other.jpg?resize=750px:*',
    'https://icatcare.org/app/uploads/2018/07/Thinking-of-getting-a-cat.png',
    'https://static01.nyt.com/images/2019/09/04/business/04chinaclone-01/merlin_160087014_de761d9a-4360-402d-a15b-ddeff775760d-superJumbo.jpg?quality=90&auto=webp',
    'https://www.aljazeera.com/mritems/imagecache/mbdxxlarge/mritems/Images/2020/4/13/ecab8c7af42a439d9043b0ade6e1f05b_18.jpg',
    'https://static.toiimg.com/thumb/msid-67586673,width-800,height-600,resizemode-75,imgsize-3918697,pt-32,y_pad-40/67586673.jpg',
    'https://hackernoon.com/hn-images/1*mONNI1lG9VuiqovpnYqicA.jpeg',
    'https://i.imgur.com/XOz8kiNb.jpg',
    'https://i.imgur.com/VF4JWfUb.jpg',
    'https://i.imgur.com/iRUzfVsb.jpg',
    'https://i.imgur.com/qZImY9jb.jpg',
    'https://i.imgur.com/jKopvGOb.jpg',
    'https://i.imgur.com/9ajLgWWb.jpg',
    'https://i.imgur.com/7ryCyvDb.jpg',
    'https://cdn.pixabay.com/photo/2014/11/30/14/11/kitty-551554_960_720.jpg',
    'https://cdn.pixabay.com/photo/2014/04/13/20/49/cat-323262_960_720.jpg',
    'https://cdn.pixabay.com/photo/2017/07/25/01/22/cat-2536662_960_720.jpg',
    'https://images.pexels.com/photos/96938/pexels-photo-96938.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260',
    'https://cdn.pixabay.com/photo/2016/06/14/00/14/cat-1455468_960_720.jpg',
    'https://cdn.pixabay.com/photo/2016/01/20/13/05/cat-1151519_960_720.jpg',
    'http://images6.fanpop.com/image/photos/36700000/Cats-image-cats-36774786-478-478.jpg'
    ]

dog_pics = ['https://hips.hearstapps.com/ghk.h-cdn.co/assets/18/08/lassie.jpg?crop=1.0xw:1xh;center,top&resize=980:*',
            'https://hips.hearstapps.com/ghk.h-cdn.co/assets/18/08/doug-the-pug.jpg?crop=1.0xw:1xh;center,top&resize=980:*',
            'https://hips.hearstapps.com/ghk.h-cdn.co/assets/18/08/1519236394-rudy-barclay.jpg?crop=0.5xw:1xh;center,top&resize=980:*',
            'https://hips.hearstapps.com/ghk.h-cdn.co/assets/18/08/jiff-pom.jpg?crop=1.0xw:1xh;center,top&resize=980:*',
            'https://hips.hearstapps.com/ghk.h-cdn.co/assets/18/08/1519167772-uga-georgia-bulldog-mascot.jpg?crop=0.44735042735042735xw:1xh;center,top&resize=980:*',
            'https://hips.hearstapps.com/ghk.h-cdn.co/assets/18/08/1519239880-smiling-pit-bull-brinks.jpg?crop=0.5xw:1xh;center,top&resize=768:*',
            'https://static.boredpanda.com/blog/wp-content/org_uploads/2014/06/none1686__700.jpg',
            'https://i.pinimg.com/236x/4b/52/54/4b525429e5152bb59311c75d3fc2476f--cute-little-dogs-i-love-dogs.jpg',
            ]

newUserMessage = """ Welcome to Capybara's Bot test!"""


insults= ["You pathetic little human can't even drink water without choking on it",
          "Go fuck yourself : )",
          "When I think about you, I touch myself. \n Meaning I rub my temples, because you give me a fucking migraine. ",
          "There's someone for everyone, and the person for you is a psychiatrist. ",
          "You may not have lost all your marbles, but there's definitely a hole in the bag",
          "You put the 'you' in Fuck You.",
          "I don't know what makes you so dumb... but it really works.",
          "How you can pack so much stupidity into one body is a medical mystery.",
          "When two people have sex, its called a twosome. \n When three people have sex, its called a threesome. \n Now I understand why you are called handsome.",
          "Don't be a pillock.",
          "Perhot' podzalupnaya",
          "Sana girsin keman yayi!",
          "Take a dump in your hand and then slap yourself.",
          "You need a high-five, one on the face",
          "I hope your fingers change into fishing hooks, and you get an itch in your balls",
          "My guess is: You have not been diagnosed yet...",
          "I would slap u but it would be animal abuse",
          ]

responses = ['It is certain.',
            'It is decidedly so.',
            'Without a doubt.',
            'Yes – definitely.',
            'You may rely on it.',
            'As I see it, yes.',
            'Most likely.',
            'Outlook good.',
            'Yes.',
            'Signs point to yes.',
            'Reply hazy, try again.',
            'Ask again later.',
            'Better not tell you now.',
            'Cannot predict now.',
            'Concentrate and ask again.',
            "Don't count on it.",
            'My reply is no.',
            'My sources say no.',
            'Outlook not so good.',
            'Very doubtful.', ]

# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Trying to make myself work'))
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')


@client.event
async def on_member_join(member):
    await client.send(f'{member} has joined the server. ')


@client.event
async def on_member_remove(member):
    await client.send(f'{member} has left the server. ')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('.hello'):
        await message.channel.send('Hello!')

    await client.process_commands(message)


# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------


@client.command()
async def say(ctx, arg):
    await ctx.send(arg)


@client.command()
async def insult(ctx):
    await ctx.send(random.choice(insults))


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command()
@commands.has_role('Manage channels')
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command()
async def cat(ctx):
    await ctx.send(random.choice(cat_pics))


@client.command()
async def dog(ctx):
    await ctx.send(random.choice(dog_pics))


@client.command()
async def randpic(ctx):
    await ctx.send('https://imgur.com/gallery/random')


@client.command()
@commands.has_permissions(administrator=True)
async def kick(member: discord.member, *, reason=None):
    print('Kicking...')
    await member.kick(reason=reason)


@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member} has been banned')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all required arguments')


@client.command()
@commands.has_permissions(administrator=True)
async def role(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)
    await ctx.send(f"{member.mention} was roled") and str(reaction.emoji) == ':white_check_mark:'



client.run('token')
