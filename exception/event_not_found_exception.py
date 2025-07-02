class EventNotFoundException(Exception):
    def __init__(self, message="Event not found. Please select a valid event."):
        super().__init__(message)
