import mongoengine

from utils.Secrets import Secrets


def db_connect():
    settings = Secrets()
    db_name = settings.get("DATABASE_NAME")
    db_host = settings.get("DATABASE_HOST")
    mongoengine.connect(db_name, host=db_host)

