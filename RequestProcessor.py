from Handler import Handler
from Request import Request


class RequestProcessor:
    def __init__(self, handlers: list[Handler]):
        self.first_handler = handlers[0]

        for i in range(len(handlers) - 1):
            handlers[i].set_successor(handlers[i + 1])

    def process_request(self, request: Request):
        approved = None
        current_handler = self.first_handler

        while approved is None:
            try:
                current_handler.success = None
                current_handler.process_request(request)
                approved = current_handler.success
            except ValueError as e:
                print(e)
                return

            if approved is True:
                return f"Request approved by {current_handler.__class__.__name__}"
            if approved is False:
                return f"Request denied by {current_handler.__class__.__name__}"

            current_handler = current_handler.successor
