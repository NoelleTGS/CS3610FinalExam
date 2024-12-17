from abc import ABC, abstractmethod

from Request import Request


class IHandler(ABC):

    @abstractmethod
    def handle_request(self, request: Request):
        pass
