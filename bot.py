from discord.ext import commands
import os

import cogs

from module import SubmitManager


class Bot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(command_prefix="!", help_command=None, **kwargs)
        self.submit_manager = SubmitManager()
        
        cogs.load(self)

    async def on_ready(self):
        print(f"Logged in as {self.user.name}")

    async def on_command_error(self, ctx: commands.Context, exception: Exception):
        if isinstance(exception, commands.CommandNotFound):
            return
        if isinstance(exception, commands.BadArgument):
            return await ctx.reply(f"⚠ 잘못된 값이 주어졌습니다.")
        
        return await ctx.reply(f"Error: {exception}")

    
if __name__ == '__main__':
    Bot().run(os.environ.get("TOKEN"))
