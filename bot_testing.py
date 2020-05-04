import discord
import time
import random
from discord.ext import commands
import token

client = commands.Bot(command_prefix = '.')

cat_pics = ['https://img.webmd.com/dtmcms/live/webmd/consumer_assets/site_images/article_thumbnails/other/cat_relaxing_on_patio_other/1800x1200_cat_relaxing_on_patio_other.jpg?resize=750px:*',
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
            ]

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Porn games'))
    print('Bot is ready')


@client.event
async def on_member_join(member):
    print(f' {member} has joined the server ')


@client.event
async def on_member_remove(member):
    print(f' {member} has left the server ')


@client.command()
async def say(ctx, arg):
    await ctx.send(arg)


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responces = ['It is certain.',
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
                 'Very doubtful.',]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responces)}')


@client.command()
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)


@client.command()
async def test1(ctx, *args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))


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
async def kick(ctx, member: discord.member, *, reason=None):
    await member.kick(reason=reason)


@client.command()
async def ban(ctx, member: discord.member, *, reason=None):
    await member.ban(reason=reason)


client.run('token')
