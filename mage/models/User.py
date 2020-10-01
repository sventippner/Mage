class User:
    """
    User object

    :parameter name
    :parameter points
    :parameter items
    """
    def __init__(self, name, points, items=None):
        self.name = name
        self.points = points
        self.items = items

    def __str__(self):
        return f"{self.name} ({self.points} Points)"
