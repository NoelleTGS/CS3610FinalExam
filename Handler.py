from abc import abstractmethod

from IHandler import IHandler
from Request import Request


class Handler(IHandler):
    def __init__(self, successor=None):
        self._successor = successor
        self._success = None

    @property
    def successor(self):
        return self._successor

    def set_successor(self, successor):
        self._successor = successor
        return successor

    def handle_request(self, request: Request):
        if not self._success and self._successor:
            self._successor.handle_request(request)

    @abstractmethod
    def process_request(self, request: Request):
        pass
