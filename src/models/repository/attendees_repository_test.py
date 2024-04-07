import pytest
from .attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Novo registro em banco de dados")
def test_insert_attendees():
    event_id = "meu_uuid_e_nois"
    attendees_info = {
        "uuid": "meu_uuid_attendee",
        "name": "attende_name",
        "email": "email@email.com",
        "event_id": event_id
    }
    attendees_repository = AttendeesRepository()
    response = attendees_repository.insert_attendee(attendees_info)
    print(response)
    

@pytest.mark.skip(reason="...")
def test_get_attendee_badge_by_id():
    attendee_id = "meu_uuid_attendee"
    attendee_repository = AttendeesRepository
    attendee = attendee_repository.get_attendee_badge_by_id(attendee_id)
    
    print(attendee)
    
