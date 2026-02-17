from abc import ABC, abstractmethod


class Repository(ABC):
    """
    Repository interface (Persistence Layer).
    
    """

    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def get(self, obj_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, obj_id, data):
        pass

    @abstractmethod
    def delete(self, obj_id):
        pass

    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value):
        pass


class InMemoryRepository(Repository):
    """
    Simple in-memory repository.
    """

    def __init__(self):
        self._storage = {}

    def _validate_object(self, obj):
        """
        Minimal validation to keep the repository consistent.
        """
        if obj is None:
            raise ValueError("Cannot store a None object.")

        if not hasattr(obj, "id"):
            raise ValueError("Stored objects must have an 'id' attribute.")

        if obj.id is None:
            raise ValueError("Object 'id' must not be None.")

    def add(self, obj):
        self._validate_object(obj)
        self._storage[obj.id] = obj

    def get(self, obj_id):
        return self._storage.get(obj_id)

    def get_all(self):
        return list(self._storage.values())

    def update(self, obj_id, data):
        
        obj = self.get(obj_id)
        if obj and isinstance(data, dict):
            for key, value in data.items():
                setattr(obj, key, value)
            self._storage[obj_id] = obj
        return obj

    def delete(self, obj_id):
        if obj_id in self._storage:
            del self._storage[obj_id]

    def get_by_attribute(self, attr_name, attr_value):
        
        return next(
            (obj for obj in self._storage.values()
             if hasattr(obj, attr_name) and getattr(obj, attr_name) == attr_value),
            None
        )
