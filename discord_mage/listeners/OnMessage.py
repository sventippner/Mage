from mage.models.User import User
from utils import data_access


class OnMessage:
    points_per_message = 1

    @staticmethod
    async def call(message):
        # ignores its own messages
        if message.author.bot:
            return

        author = data_access.find_user_by_discord_message(message)
        if not author:
            author = User.from_discord(message.author.id, message.guild.id)
            author.save()
        if not message.content.startswith(data_access.get_prefix(message.guild.id)):
            OnMessage.action_increase_user_points(author)

    @staticmethod
    def action_increase_user_points(user):
        user.points += OnMessage.points_per_message
        user.save_this(set__points=user.points)
