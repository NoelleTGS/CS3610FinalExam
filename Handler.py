from abc import abstractmethod

from IHandler import IHandler
from Request import Request, Level


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

    @success.setter
    def success(self, value):
        self._success = value

    def set_successor(self, successor):
        self._successor = successor
        return successor

    def handle_request(self, request: Request):
        if not self._success and self._successor:
            self._successor.handle_request(request)

    def check_constraints(self, request: Request):
        if request.employee_level == Level.Intern and request.days > 4:
            self._success = False
            print("Interns can only request up to 4 days at once.")
            return False

        if request.employee_level == Level.Junior and request.days > 14:
            self._success = False
            print("Juniors can only request up to 2 weeks at once.")
            return False

        if request.employee_level == Level.Senior and request.days > 28:
            self._success = False
            print("Seniors can only request up to 4 weeks at once.")
            return False

        return True

    @abstractmethod
    def process_request(self, request: Request):
        pass
