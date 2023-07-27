from enum import Enum

class StatusCode(Enum):
    SUCCESS = 200
    BAD_SYNTAX = 400
    AUTH_FAILED = 401
    USAGE_LIMIT_REACHED = 402
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    SERVER_ERROR = 500
    SERVICE_UNAVAILABLE = 503

    def __str__(self):
        return {
            StatusCode.SUCCESS: "The request was successful.",
            StatusCode.BAD_SYNTAX: "The request had bad syntax or was inherently impossible to be satisfied.",
            StatusCode.AUTH_FAILED: "Authentication failed, probably because of invalid/missing API key.",
            StatusCode.USAGE_LIMIT_REACHED: "The usage limit has been reached, either you exceeded per day requests limits or your balance is insufficient.",
            StatusCode.FORBIDDEN: "You are not authorized to perform this operation.",
            StatusCode.NOT_FOUND: "The requested resource was not found.",
            StatusCode.METHOD_NOT_ALLOWED: "The requested method was not found.",
            StatusCode.SERVER_ERROR: "Ops. Something went wrong.",
            StatusCode.SERVICE_UNAVAILABLE: "Our system is a bit busy at the moment and your request can’t be satisfied.",
        }.get(self, "Unknown status code.")
