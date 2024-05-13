#!/usr/bin/python3
import json 
list_of_dicts = []

class FileStorage:
    def __init__(self, filename='storage.json'):
        self.filename = filename
        self.data = {}

    def save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, indent=4)

    def load(self):
        try:
            with open(self.filename, 'r') as f:
                self.data = json.load(f)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            self.data = {}

    def add_user(self, obj):
        self.load()
        if 'Users' not in self.data:
            self.data['Users'] = list_of_dicts
        self.data['Users'].append(obj.to_dict())

    def add_state(self, obj):
        self.load()
        if 'States' not in self.data:
            self.data['States'] = list_of_dicts
        self.data['States'].append(obj.to_dict())  


 