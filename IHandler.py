from abc import ABC, abstractmethod


class IHandler(ABC):

    @abstractmethod
    def handle_request(self, request):
        pass
