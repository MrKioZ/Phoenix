import discord
from discord.ext import commands
from config import Embed_Color
from config import WELCOME_MODE
from config import DEFAULT_ROLE_ID
from config import WELCOME_Channel_ID

class Greetings(commands.Cog, name='Greeting'):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        print('[Cogs] Greetings has been loaded Successfully!')

    @commands.Cog.listener()
    async def on_member_join(self, member):


        if DEFAULT_ROLE_ID:
            role = discord.utils.get(member.guild.roles, id=DEFAULT_ROLE_ID)
            await member.add_role(role)

            embed = discord.Embed(color=Embed_Color)
            help_desc = f"""
            Welcome to uPay's Public Discord, {member.mention}!


            """

            embed.add_field(name='Welcome to Upay\'s discord server!', value=help_desc)

            if WELCOME_MODE.lower() == 'dm':
                await member.send(embed=embed)
            elif WELCOME_MODE.lower() == 'channel':
                if Welcome_Channel_ID:
                    channel = bot.get_channel(Welcome_Channel_ID)
                    await channel.send(embed=embed)
            elif WELCOME_MODE.lower() == 'both':
                if Welcome_Channel_ID:
                    channel = bot.get_channel(Welcome_Channel_ID)
                    await channel.send(embed=embed)
                    await member.send(embed=embed)
            else:
                print('[Alert] Could not send a welcome message because "WELCOME_MODE" is not Correct or Undefine please Choose between (DM / Channel / Both)')
