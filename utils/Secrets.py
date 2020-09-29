from utils.EnvLoader import EnvLoader


class Secrets(EnvLoader):

    def __init__(self):
        self = EnvLoader("secrets/secrets.env")
