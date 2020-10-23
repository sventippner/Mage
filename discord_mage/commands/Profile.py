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

        await context.send(Profile.action(user))

    @staticmethod
    def action(user):
        msg = f"Level: **{user.level}**"
        if user.level == User.max_level:
            msg += " (MAX)"

        msg += f"\nPoints: **{user.points}**\n\n"

        if user.level < User.max_level:
            points_needed = User.level_generator[user.level + 1] - user.points
            msg += f"\nPoints needed for Level-Up: {points_needed}"

        if user.items:
            msg += f"\n**{len(user.items)} Items:**"
            for item in user.items:
                msg += f'<Todo> \n{item}'

        return msg
