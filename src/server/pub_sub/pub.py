from queue import Queue
from threading import Lock


class Publisher:
    def __init__(self):
        self.subscribers = []
        self.lock = Lock()
    
    def subscribe(self, subscriber):
        with self.lock:
            self.subscribers.append(subscriber)
    
    def unsubscribe(self, subscriber):
        with self.lock:
            self.subscribers.remove(subscriber)
    
    def send(self, message):
        with self.lock:
            for subscriber in self.subscribers:
                subscriber.queue.put(message)