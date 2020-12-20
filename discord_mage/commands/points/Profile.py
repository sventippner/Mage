from mage.models.Item import Item
from mage.models.Server import Server
from mage.models.User import User
from utils import data_access


class Profile:
    aliases = []
    brief = 'displays profile'
    description = 'displays your current account profile for this server'

    @staticmethod
    async def call(context):
        """ this function is executed by a discord message """
        user = data_access.find_user_by_discord_message(context.message)
        server = data_access.find_one(Server, discord_guild_id=context.guild.id)

        await context.send(Profile.action(server, user, mention=context.message.author.mention))

    @staticmethod
    def action(server, user, mention=None):
        if not mention:
            mention = user.name
        msg = f"{mention}\n"

        msg += f"Level: **{user.level}**"
        if user.level == User.max_level:
            msg += " (MAX)"

        msg += f"\n{server.points_name}: **{user.points}**"

        if user.level < User.max_level:
            points_needed = User.level_generator[user.level + 1] - user.points
            msg += f"\n{server.points_name} needed for Level-Up: {points_needed}"

        if user.items:
            msg += f"\n\n**Items:**"
            for item in user.items:
                msg += f"\n\t{item} ({user.items[item]})"

        return msg
