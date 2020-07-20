import discord
import random
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix='.')


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
