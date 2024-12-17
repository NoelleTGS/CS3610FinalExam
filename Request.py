from enum import Enum


class Level(Enum):
    Intern = 1
    Junior = 2
    Senior = 3


class Reason(Enum):
    Regular = 1
    Critical = 2
    Special = 3


class Request:
    def __init__(self, days: int, level: Level, reason: Reason):
        self.days = days
        self.employee_level = level
        self.reason = reason
