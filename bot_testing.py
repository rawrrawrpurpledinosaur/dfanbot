import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')


@client.event
async def on_ready():
    print('client is ready')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswitch('.hello'):
        msg = 'Hello (0.author.mention)'.format(message)
        await client.send_message(message.channel, msg)

        
@client.event
async def on_member_join(member):
    await member.send(f'(member) has joined the server. ')

@client.event
async def on_member_remove(member):
    await member.send(f'(member) has left the server. ')


@client.command()
async def ping(ctx):
    await ctx.send('pong')


client.run('NzA2MDc4ODE2OTI5NTc5MDU4.Xq1BNw.6yVU4NPDEMJNjRzglRNomF6-u6M')