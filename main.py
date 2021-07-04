from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option, create_choice

# Put your Token here
TOKEN = '' 

# Put the servers' IDs here
GUILD_IDS = [
    
]

bot = commands.Bot(command_prefix=None)
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print('Ready!')

@slash.slash(
    name='role-join',
    description='Choose a role to assign.',
    guild_ids=GUILD_IDS,
    options=[
        create_option(
            name='role',
            description='Elige un rol.',
            option_type=3, # 3 for String
            required=True,
            choices=[

                # As many as needed
                create_choice(
                    name='', # Displayed text
                    value='' # Role ID as String
                )
            ]
        )
    ]
)
async def _role_join(ctx, **kwargs):
    try:
        role_id = int(kwargs["role"])
    except:
        await ctx.send(content=f'Usage: /role-join role: <role>')
    else:
        
        # It is recommended to have some control over who uses the command

        try:
            user = ctx.author
            role = ctx.guild.get_role(role_id)
            await user.add_roles(role)
            await ctx.send(content=f'`{role}` assigned to {user.mention}.')
        except Exception as e:
            print(e)
            await ctx.send(content=f'Error.')

bot.run(TOKEN)