from abc import abstractmethod

from IHandler import IHandler
from Request import Request, Level


def check_constraints(request: Request):
    if request.employee_level == Level.Intern and request.days > 4:
        raise ValueError("Interns can only request up to 4 days at once.")

    if request.employee_level == Level.Junior and request.days > 14:
        raise ValueError("Juniors can only request up to 2 weeks at once.")

    if request.employee_level == Level.Senior and request.days > 28:
        raise ValueError("Seniors can only request up to 4 weeks at once.")


class Handler(IHandler):
    def __init__(self, successor=None):
        self._successor = successor
        self._success = None

    @property
    def successor(self):
        return self._successor

    @property
    def success(self):
        return self._success

    def set_successor(self, successor):
        self._successor = successor
        return successor

    def handle_request(self, request: Request):
        if not self._success and self._successor:
            self._successor.handle_request(request)

    @abstractmethod
    def process_request(self, request: Request):
        pass
