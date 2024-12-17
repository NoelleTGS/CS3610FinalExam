from enum import Enum


# The level of the employee at the company
# Interns can only take off up to 4 days at once.
# Juniors can take off up to 2 weeks at once.
# Seniors can take off up to 4 weeks at once.
class Level(Enum):
    Intern = 1
    Junior = 2
    Senior = 3


# The severity of the reason for the leave
# Regular reasons will only be approved occasionally.
# Critical reasons will be approved most of the time.
# Special reasons will always be approved, as it is
#     reserved for reasons such as company events.
class Reason(Enum):
    Regular = 1
    Critical = 2
    Special = 3


class Request:
    def __init__(self, days: int, level: Level, reason: Reason):
        self.days = days
        self.employee_level = level
        self.reason = reason

    def __str__(self):
        return f"Request for {self.days} day(s) by a(n) {self.employee_level.name} for reason {self.reason.name}"
