from Handler import TeamLeader, ProjectLeader, HumanResources, Manager
from Request import Request, Level, Reason
from RequestProcessor import RequestProcessor

handlers = [TeamLeader(), ProjectLeader(), HumanResources(), Manager()]

processor = RequestProcessor(handlers)

requests = [
    Request(1, Level.Intern, Reason.Regular),
    Request(14, Level.Intern, Reason.Critical),
    Request(10, Level.Junior, Reason.Critical),
    Request(15, Level.Junior, Reason.Regular),
    Request(20, Level.Senior, Reason.Special),
    Request(999, Level.Senior, Reason.Regular)
]

for request in requests:
    print(request)
    print(processor.process_request(request))
    print("\n")
