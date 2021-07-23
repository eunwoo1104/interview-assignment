import datetime
from discord.ext import commands
from typing import TYPE_CHECKING, Optional
from module import to_timeformat

if TYPE_CHECKING:
    from bot import Bot


class Review(commands.Cog):
    """
    봇 심사 Cog 입니다.
    """

    def __init__(self, bot: "Bot"):
        self.bot = bot

    @commands.command(name="todo")
    async def todo(self, ctx: commands.Context, query: Optional[int] = None):
        if query and query < 1:
            return await ctx.reply("⚠ 잘못된 `query` 값입니다. `query`는 1 이상이어야 합니다.")
        if not query:
            subs = self.bot.submit_manager.get_submits()
            return await ctx.reply(f"TODOs: 총 {len(subs)}개\n\n"+'\n'.join([f"#{i+1}: `{x.id}`" for i, x in enumerate(subs.values())]))
        bot = self.bot.submit_manager.get_submit(query)
        if not bot:
            return await ctx.reply("⚠ 해당 봇은 존재하지 않습니다.")
        oauth2 = f"https://discord.com/oauth2/authorize?client_id={bot.id}&scope=bot&permissions=0&guild_id=653083797763522580&disable_guild_select=true"
        await ctx.reply(f"TODO: `{bot.id}`\n"
                        f"Date: {to_timeformat(datetime.datetime.fromtimestamp(bot.date))}\n"
                        f"Invite: {oauth2}")

    @commands.command(name="approve")
    async def approve(self, ctx: commands.Context, query: int):
        bot = self.bot.submit_manager.approve(query)
        if not bot:
            return await ctx.reply("⚠ 해당 봇은 존재하지 않습니다.")
        await ctx.reply("✅ 성공적으로 해당 봇 신청을 승인했습니다.")

    @commands.command(name="deny")
    async def deny(self, ctx: commands.Context, query: int):
        bot = self.bot.submit_manager.deny(query)
        if not bot:
            return await ctx.reply("⚠ 해당 봇은 존재하지 않습니다.")
        await ctx.reply("✅ 성공적으로 해당 봇 신청을 거부했습니다.")


def setup(bot: "Bot"):
    bot.add_cog(Review(bot))
