#!/usr/bin/python3
import json
import uuid
class BaseModel:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, adict):
        return cls(**adict)

    def to_json(self):
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str):
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def get_by_name(cls, name):
        """Retrieve an object by its name."""
        # Load data from JSON file
        with open(cls.file_path, 'r') as file:
            data = json.load(file)

        # Find object by name
        for obj in data:
            if obj.get('name') == name:
                return cls(**obj)

        return None
    


class User(BaseModel):
    latest = uuid.uuid4()
    def __init__(self, user_id, username, email, timeOfChange):
        super().__init__(user_id=user_id, username=username, email=email, timeOfchange=timeOfChange)

class State(BaseModel):
    latest = uuid.uuid4()
    def __init__(self, state_id, state_name, timeOfChange):
        super().__init__(state_id=state_id, state_name=state_name, timeOfchange=timeOfChange)

class City(BaseModel):
    latest = uuid.uuid4()
    def __init__(self, city_id, city_name, state_name, timeOfChange):
        super().__init__(city_id=city_id, city_name=city_name, state_name=state_name, timeOfchange=timeOfChange)

class Place(BaseModel):
    latest = uuid.uuid4()
    def __init__(self, place_id, place_name, city_name,  timeOfChange):
        super().__init__(place_id=place_id, place_name=place_name, city_name=city_name, timeOfchange=timeOfChange)