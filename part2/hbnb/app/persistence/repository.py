#!/usr/bin/python3

class InMemoryRepository:
    """Store objects by id in memory."""

    def __init__(self):
        self._data = {}

    def add(self, obj):
        self._data[obj.id] = obj
        return obj

    def get(self, obj_id):
        return self._data.get(obj_id)

    def delete(self, obj_id):
        return self._data.pop(obj_id, None)

    def list_all(self):
        return list(self._data.values())
