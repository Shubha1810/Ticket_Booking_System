class InvalidBookingIDException(Exception):
    def __init__(self, message="Invalid booking ID."):
        super().__init__(message)
