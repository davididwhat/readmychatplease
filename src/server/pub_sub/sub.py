import threading
from queue import Queue


class Subscriber:
    def __init__(self, name):
        self.name = name
        self.queue = Queue()
        
    def start_listening(self):
        thread = threading.Thread(target=self._listen)
        thread.daemon = True
        thread.start()
    
    def _listen(self):
        while True:
            message = self.queue.get()
            print(f"Subscriber {self.name} received: {message}")
            self.queue.task_done()