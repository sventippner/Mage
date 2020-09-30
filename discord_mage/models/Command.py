

class Command:

    @property
    def aliases(self):
        raise NotImplementedError

    @property
    def brief(self):
        raise NotImplementedError

    @property
    def description(self):
        raise NotImplementedError
