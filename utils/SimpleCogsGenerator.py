# Author: Martin Ludwig
# Date: 29.05.2020

from utils.PythonCodeGenerator import PythonCodeGenerator


class SimpleCogsGenerator:
    # class and file name
    __name = "DSC"

    # list with additional imports
    __imports = [
    ]

    def __init__(self, name=None):
        if name:
            self.__name = name
        self.__code = PythonCodeGenerator()
        self.__write_imports()
        self.__write_class_header()

    def __write_imports(self):
        # this import is required
        self.__code.write_line("from discord.ext import commands")
        # add additional imports
        for i in self.__imports:
            self.__code.write_line(i)
        self.__code.newline()
        self.__code.newline()

    def __write_class_header(self):
        self.__code.write_line(f"class {self.__name}(commands.Cog):")
        self.__code.tab()
        self.__code.write_line("def __init__(self, client):")
        self.__code.tab()
        self.__code.write_line("self.client = client")
        self.__code.stab()

    def __write_setup(self):
        self.__code.newline()
        self.__code.newline()
        self.__code.stab()
        self.__code.write_line("def setup(client):")
        self.__code.tab()
        self.__code.write_line(f"client.add_cog({self.__name}(client))")
        self.__code.newline()

    def add_cog(self, name, output, brief="", description=""):
        cog_annotation = f'@commands.command(brief="{brief}", description="{description}")'
        cog_header = f'async def {name}(self, context):'
        cog_return = f'await context.send(f\'{output}\')'
        self.__code.newline()
        self.__code.write_line(cog_annotation)
        self.__code.write_line(cog_header)
        self.__code.tab()
        self.__code.write_line(cog_return)
        self.__code.stab()

    # writes file
    # returns generated code
    def write_file(self, dirpath, force_overwrite=False):
        self.__write_setup()
        return self.__code.generate(dirpath, f"{self.__name}.py", force_overwrite)
