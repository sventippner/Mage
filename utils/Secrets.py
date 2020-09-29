from utils.EnvLoader import EnvLoader


class Secrets(EnvLoader):
    """ Reads secrets.env """
    def __init__(self):
        self = EnvLoader("secrets/secrets.env")