from typing import List
from pathlib import Path


class Parser:
    extensions: List[str] = []

    def valid_extension(extension):
        if extension in self.extensions:
            return extension