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

        await context.send(Profile.action(server, user))

    @staticmethod
    def action(server, user):
        msg = f"Level: **{user.level}**"
        if user.level == User.max_level:
            msg += " (MAX)"

        msg += f"\n{server.points_name}: **{user.points}**"

        if user.level < User.max_level:
            points_needed = User.level_generator[user.level + 1] - user.points
            msg += f"\n{server.points_name} needed for Level-Up: {points_needed}"

        if user.items:
            msg += f"\n\n**Items:**"
            for item, amount in user.items.items():
                msg += f'\n<Todo> {amount}x {item}'

        return msg
