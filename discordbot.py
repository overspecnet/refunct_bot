from discord.ext import commands
import speedrun
import refunct
import technique
import os
import traceback
import time

bot = commands.Bot(command_prefix='!')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def c(ctx):
    await ctx.send('The race will begin in 10 seconds!')
    time.sleep(5)
    await ctx.send('The race will begin in 5 seconds!')
    time.sleep(2)
    await ctx.send("3")
    time.sleep(1)
    await ctx.send("2")
    time.sleep(1)
    await ctx.send("1")
    time.sleep(1)
    await ctx.send("Go!")

@bot.command()
async def ranking(ctx, arg):
    if "雑談" in str(ctx.channel) or "記録確認所" in str(ctx.channel):
        if "Refunct" in str(ctx.guild):
            send_list = refunct.get_ranking(arg)
        else:
            send_list = speedrun.get_ranking(arg)
        send_str = '\n'.join(send_list)
        await ctx.send(send_str)

@bot.command()
async def tech(ctx, arg):
    if "雑談" in str(ctx.channel):
        if "Refunct" in str(ctx.guild):
            send_list = technique.get_tech(arg)
            send_str = '\n'.join(send_list)
            await ctx.send(send_str)

@bot.command()
async def test(ctx):
    if "ぐにぴったん" in str(ctx.guild):
        await ctx.send(ctx.guild)

bot.run(token)
