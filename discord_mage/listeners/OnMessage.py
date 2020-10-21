from mage.models.User import User


class OnMessage:
    points_per_message = 1

    async def call(self, client, message):
        # ignores its own messages
        if message.author == client.user:
            return

#        author = User.find(discord_user_id=message.author.id, discord_guild_id=message.guild.id)
#        self.action_increase_user_points(author)

    def action_increase_user_points(self, user):
        user.points += self.points_per_message
        user.update()
