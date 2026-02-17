import uuid
from datetime import datetime


class BaseModel:
    """
    Base model providing:
    - UUID id
    - created_at
    - updated_at
    - save()
    - to_dict()
    """

    def __init__(self, **kwargs):
        self.id = kwargs.get("id", str(uuid.uuid4()))
        self.created_at = kwargs.get("created_at", datetime.utcnow())
        self.updated_at = kwargs.get("updated_at", datetime.utcnow())

    def save(self):
        
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "__class__": self.__class__.__name__,
        }
