import uuid
from src.models.repository.events_repository import EventRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class EventHandler:
    def __init__(self) -> None:
        self.__events_repository = EventRepository()
        
    
    def register(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        body["uuid"] = str(uuid.uuid4())
        self.__events_repository.insert_event(body)
        
        return HttpResponse(
            body={"event_id": body["uuid"]},
            status_code=200
        )
        
        