from discord_mage.commands.reactions.buttons.ButtonMaker import ButtonMaker


class MakeRoleButtons(ButtonMaker):
    aliases = ['makebuttons', 'makerolebuttons']
    brief = "members can toggle roles"
    description = "creates emoji buttons (reactions) below the message. Members can toggle roles upon reaction."

    is_distinct = False