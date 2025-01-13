import os
from typing import Optional

from watchdog.events import FileSystemEventHandler


class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, filename: str):
        self.filename = os.path.abspath(filename)
        self._new_line = None

    def on_modified(self, event) -> None:
        if os.path.abspath(event.src_path) == self.filename:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                if lines:
                    self._new_line = lines[-1].strip()

    def get_new_line(self) -> Optional[str]:
        return self._new_line