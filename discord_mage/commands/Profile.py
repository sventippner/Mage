from utils import data_access


class Profile:
    aliases = []
    brief = 'displays profile'
    description = 'displays your current account profile for this server'

    async def discord_call(self, context, message):
        """ this function is executed by a discord message """
        user = data_access.find_user_by_discord_message(message)

        await context.send(self.action(user))

    def action(self, user):
        msg = f"Level: **{user.level}**"
        if user.level == user.max_level:
            msg += " (MAX)"

        msg += f"\nPoints: **{user.points}**\n\n"

        if user.level < user.max_level:
            msg += "\nPoints needed for Level-Up: <Todo>"

        if user.items and len(user.items) > 0:
            msg += f"\n**{len(user.items)}Items:**"
            for item in user.items:
                msg += f'<Todo> \n{item}'

        return msg
