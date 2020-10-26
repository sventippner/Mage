# Author: Martin Ludwig
# Date: 29.05.2020
#
# inspired by fredrik lundh, march 1998
# http://effbot.org/zone/python-code-generator.htm

import os
from datetime import datetime
from pathlib import Path


class PythonCodeGenerator:

    def __init__(self, tab="\t"):
        self.__tab = tab
        self.__code = []
        self.__lines = 0
        self.__indents = 0
        self.write_line("# This code is auto-generated.")
        self.write_line(f"# Date: {datetime.now()}")
        self.write_line("# ")
        self.write_line("# Changes to this file will be lost if the code is regenerated.")
        self.newline()

    def count_indents(self):
        return self.__indents

    def get_code(self):
        return "\n".join(self.__code)

    def get_tab(self):
        return self.__tab

    def write(self, string):
        self.__code[self.__lines] += string

    def write_line(self, string):
        self.__code.append(self.__tab * self.__indents + string)
        self.__lines += 1

    def newline(self):
        self.write_line("")

    def tab(self):
        self.__indents = self.__indents + 1

    # shift tab
    def stab(self):
        if self.__indents == 0:
            raise SyntaxError("[PythonCodeGenerator] Indentation error: Cannot further shift-tab")
        self.__indents = self.__indents - 1

    # writes file
    # returns generated code
    def generate(self, dirpath="", filename="", force_overwrite=False):
        file = f"{dirpath}/{filename}"
        if not force_overwrite and os.path.isfile(file):
            raise FileExistsError(f"[PythonCodeGenerator] File {file} already exists.")

        code = self.get_code()

        Path(dirpath).mkdir(parents=True, exist_ok=True)

        with open(file, 'w+', encoding='utf-8') as f:
            f.write(code)

        return code