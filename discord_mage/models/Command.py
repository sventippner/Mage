import abc

class Command(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def discord_call(self, input):
        """ this function is executed by discord message """
        return


    @property
    def aliases(self):
        """ The list of aliases the command can be invoked under. """
        raise NotImplementedError

    @property
    def brief(self):
        """ The short help text for the command. """
        raise NotImplementedError

    @property
    def description(self):
        """ The message prefixed into the default help command. """
        raise NotImplementedError
