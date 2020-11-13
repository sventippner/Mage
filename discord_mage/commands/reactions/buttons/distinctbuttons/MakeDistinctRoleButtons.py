from discord_mage.commands.reactions.buttons.ButtonMaker import ButtonMaker


class MakeDistinctRoleButtons(ButtonMaker):
    aliases = ['makedistinctbuttons', 'makedistinctrolebuttons']
    brief = "members can toggle distinct roles"
    description = "creates emoji buttons (reactions) below the message. Members can toggle roles upon reaction."

    is_distinct = True