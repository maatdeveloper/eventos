from src.http_types.http_response import HTTPResponse
from src.errors.error_types.http_conflict import HttpConflictError
from src.errors.error_types.http_not_found import HttpNotFoundError

def handle_error(error: Exception) -> HTTPResponse:
    if isinstance(error, (HttpConflictError, HttpNotFoundError)):
        return HTTPResponse(
            body={
                "errors": [{
                    "title": error.name,
                    "details": error.message,
                }]
            },
            status_code=error.status_code
        )
    return HTTPResponse(
        body={
            "errors": [{
                "title": "error",
                "details": str(error)
            }]
        }
    )
    
    