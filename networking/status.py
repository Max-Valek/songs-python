# Information about API responses
class Status:

    # Returns a message associated with a specified status code.
    @staticmethod
    def get_message(status_code):
        match status_code:
            case 200: return "Success!"
            case 400: return "The request had bad syntax or was inherently impossible to be satisfied."
            case 401: return "Authentication failed, probably because of invalid/missing API key."
            case 402: return "The usage limit reached."
            case 403: return "You are not authorized to perform this operation."
            case 404: return "The requested resource was not found."
            case 405: return "The requested method was not found."
            case 500: return "External server error."
            case 503: return "Server is busy right now. Try again later."
            case _: return "Unknown error."
