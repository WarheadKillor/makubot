import discord
from discord.ext import commands
from utils import Config

import subprocess
import sys
import traceback

class Settings():
    def __init__(self, bot):
        self.bot = bot

    @commands.is_owner()
    @commands.command(hidden=True)
    async def defaultprefix(self, ctx, prefix: str):
        ''' changes the default prefix '''
        try:
            Config.set_prefix(prefix)
        except ValueError:
            await ctx.channel.send(f'Prefix invalid or not all Values set properly.')
        
        await ctx.channel.send(f'Prefix changed to `{prefix}`')

    @commands.is_owner()
    @commands.command(hidden=True)
    async def exec(self, ctx, *command: str):
        try:
            with subprocess.Popen([*list(command)], stdout=subprocess.PIPE) as proc:
                out = proc.stdout.read().decode()[0:1994] #max 2000 signs per message
                await ctx.channel.send("```" + out + "```")
        except:
            await ctx.channel.send(f'Command `{command}` failed.')
            traceback.print_exc()
    
    @commands.is_owner()
    @commands.command(hidden=True)
    async def restart(self, ctx):
        await ctx.channel.send(f'Restarting..')
        sys.exit()
   

    
    