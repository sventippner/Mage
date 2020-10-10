class User:
    """
    User object

    :parameter name
    :parameter points
    :parameter items
    """
    def __init__(self, user_id, server_id, points=0, items=None, pvp_status=False):
        self.user_id = user_id
        self.server_id = server_id
        self.points = points
        self.items = items
        self.pvp_status = pvp_status

    def __str__(self):
        return f"User ID:{self.user_id} ({self.points} Points)"
