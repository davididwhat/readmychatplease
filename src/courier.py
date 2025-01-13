from utils import install_modules

modules: list = [
    "watchdog"
]

install_modules(modules)

import os
import socket
import threading
import time

from watchdog.observers import Observer

from server import FileChangeHandler, ServerClient
from utils import VarFetch


def watch_file(filename: str, client: ServerClient) -> None:
    file_path = os.path.abspath(filename)
    directory = os.path.dirname(file_path)

    event_handler = FileChangeHandler(file_path)

    observer = Observer()
    observer.schedule(event_handler, path=directory, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(0.1)
            new_line = event_handler.get_new_line()
            if new_line:
                client.send(new_line)
                event_handler._new_line = None
    except KeyboardInterrupt:
        observer.stop()

def main():
    cfg = VarFetch()
    cfg.load_config(keys=['ADDRESS', 'PORT', 'TEMP_FILE'])

    config: dict[str, str] = cfg.config()
    host = config['ADDRESS']
    port = config['PORT']
    temp = config['TEMP_FILE']

    client = ServerClient(host, port, socket.AF_INET, socket.SOCK_STREAM)
    client.connect_to_server()

    watch_thread = threading.Thread(target=watch_file, args=(temp, client))
    watch_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down...")
        client.close_connection()
        watch_thread.join()

if __name__ == "__main__":
    main()