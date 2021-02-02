import re

from yaml import load
from yaml import FullLoader
from collections.abc import Mapping


class Content(Mapping):
    __delimiter = r"^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    @classmethod
    def load(cls, string):
        _, fm, content = cls.__regex.split(string, 2)

        metadata = load(fm, Loader=FullLoader)
        cls(metadata, content)
