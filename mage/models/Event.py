from mongoengine import Document, StringField, DateTimeField


# todo: rewards

class Event(Document):
    """ Event
    :param start_date: DateTime when the event started.
    :param end_date = DateTime when the event ends.
    :param duration = DateTime how long the event lasts.
    :param reward = Rewards
    """

    start_date = DateTimeField()
    end_date = DateTimeField()
    duration = DateTimeField()
    reward = StringField()

    def __init__(self):
        pass

