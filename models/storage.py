#!/usr/bin/python3
import json 
userslist = []
statelist = []
citylist = []
placelist = []

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
            self.data['Users'] = userslist
        self.data['Users'].append(obj.to_dict())

    def add_state(self, obj):
        self.load()
        if 'States' not in self.data:
            self.data['States'] = statelist
        self.data['States'].append(obj.to_dict()) 


    def add_city(self, obj):
        self.load()
        if 'Cities' not in self.data:
            self.data['Cities'] = citylist
        self.data['Cities'].append(obj.to_dict())  


    def add_place(self, obj):
        self.load()
        if 'Place' not in self.data:
            self.data['Place'] = placelist
        self.data['Place'].append(obj.to_dict())  


 