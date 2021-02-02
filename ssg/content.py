import re

from yaml import load
from yaml import FullLoader
from collections.abc import Mapping


class Content(Mapping):
    __delimiter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    def load(self):
        self.__regex.split()