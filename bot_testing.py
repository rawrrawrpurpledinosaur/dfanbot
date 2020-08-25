import os
from replies import responses, insults, cat_pics, dog_pics
import discord
import random
from discord.ext import commands, tasks
import time
import badword
from badword import list
client = commands.Bot(command_prefix='.')
client.remove_command("help")

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


@client.event
async def on_message(message):
    for word in badword.list:
        if word in message.content.lower():
            await message.channel.purge(limit=1)
            await message.channel.send(f"{message.author.mention}! Please refrain from swearing")
    await client.process_commands(message)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Trying to make myself work'))
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')


@client.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = 'Welcome {0.mention} to {1.name}! :confetti_ball: '.format(member, guild)
        await guild.system_channel.send(to_send)
        role = discord.utils.get(member.server.roles, id="<706108630277292053>")
        await member.add_roles(member, role)

@client.event
async def on_member_remove(member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = 'Bye! {0.mention} :cry:'.format(member)
        await guild.system_channel.send(to_send)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'Please pass in all required arguments')
        time.sleep(2)
        await ctx.channel.purge(limit=1)

#Cogs
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    client.load_extension(f'example.{extension}')
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-   3]}')


#commands
@client.command()
async def hello(message):
    """Says hello"""
    await message.channel.send('Hello!')


@client.command()
async def users(message):
    """Shows number of users in the server"""
    id = client.get_guild(706081251848618045)
    await message.channel.send(f"```Number of Members: {id.member_count}```")


@client.command()
async def roll(ctx):
    x = [1, 2, 3, 4, 5, 6]
    await ctx.send(random.choice(x))


@client.command()
async def say(ctx, arg):
    await ctx.send(arg)


@client.command()
async def porngif(message):
    await message.channel.send("https://giphy.com/gifs/rick-roll-lgcUUCXgC8mEo")


@client.command()
async def insult(ctx):
    await ctx.send(random.choice(insults))


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)
    channel = client.get_channel(731473025223884851)
    await channel.send(f"{amount} messages cleared by {ctx.author.mention}")
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have the permissions to clear messages!")


@client.command()
async def ping(ctx):
    """Use this to ping my ass"""
    if round(client.latency * 1000 <= 260):
        await ctx.send(f"Pong! {round(client.latency * 1000)}ms, I'm fast as fk boi")
    elif round(client.latency * 1000 > 260):
        await ctx.send(f"**Crawling**, p...pong! {round(client.latency * 1000)} ms")


@client.command()
async def coinflip(message):
    coin = ["heads", "tails"]
    flip = random.choice(coin)
    await message.channel.send(flip)

@client.command()
async def dog(ctx):
    await ctx.send(random.choice(dog_pics))


@client.command()
async def cat(ctx):
    await ctx.send(random.choice(cat_pics))

@client.command()
async def slap(ctx, member: discord.Member, reason="no reason"):
    await ctx.send(f'{member.mention} has been slapped by {ctx.author.mention} for {reason}')

class MemberRoles(commands.MemberConverter):
    async def convert(self, ctx, argument):
        member = await super().convert(ctx, argument)
        return [role.name for role in member.roles[1:]] # Remove everyone role!

@client.command()
async def roles(ctx, *, member: MemberRoles):
    """Tells you a member's roles."""
    await ctx.send('I see the following roles: ' + ', '.join(member))


@client.command()
@commands.has_permissions(administrator=True)
async def repeat(ctx, limit: int):
    x = limit
    while x > 0:
        await ctx.send("@everyone")
        time.sleep(1)
        x-=1

@client.command()
async def help(ctx):
    embed = discord.Embed(title="Here is a list of all the commands: ", colour=discord.Colour(0xbe5ac6))
    embed.add_field(name="Moderation commands: ", value=".role, .unrole, .kick, .ban")
    await ctx.send(embed=embed)
client.run(read_token())
