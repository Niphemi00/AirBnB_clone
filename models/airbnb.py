#!/usr/bin/python3
import cmd
from index import *
from datetime import datetime
from storage import FileStorage
file_storage = FileStorage()
class MyCmdInterpreter(cmd.Cmd):
    prompt = '(hbnb) '
    def do_create(self, arg):
        """Create a new object"""
        args = arg.split()
        if len(args) <= 1:
            print("Usage: create <class_name> <attributes>")
            return
        
        class_name = args[0]
        attributes = args[1:]
        created_at = datetime.now().strftime("%A %d %B %Y at %H:%M:%S")
        if class_name == 'User':
            user_id = str(User.latest)
            user_name, email = attributes
            new_user = User(user_id=user_id, username=user_name, email=email, created_at=str(created_at))
            if new_user:
                file_storage.add_user(new_user)
                # file_storage.save()
                print("New user Created!!")
            else:
              print("Failed to create user. Please try again.")



        elif class_name == 'State':
            state_id = str(State.latest)
            state_name = attributes
            new_state = State(state_id=state_id, state_name=state_name[0], created_at=str(created_at))
            if new_state:
                file_storage.add_state(new_state)
                # file_storage.save()
                print("New state Created!!")
            else:
              print("Failed to create State. Please try again.")


        elif class_name == 'City':
            city_id = str(City.latest)
            city_name, state_name = attributes
            new_city = City(city_id=city_id, city_name=city_name, state_name=state_name, created_at=str(created_at))
            if new_city:
                file_storage.add_city(new_city)
                # file_storage.save()
                print("New city Created!!")
            else:
              print("Failed to create State. Please try again.")

        elif class_name == 'Place':
            place_id = str(Place.latest)
            place_name, city_name = attributes
            new_place = Place(place_id=place_id, place_name=place_name, city_name=city_name, created_at=str(created_at))
            if new_place:
                file_storage.add_place(new_place)
                # file_storage.save()
                print("New place Created!!")
        # 
        file_storage.save()


    def do_quit(self, arg):
        """Exit the command interpreter"""
        print("Exiting the console...")
        return True

if __name__ == '__main__':
    MyCmdInterpreter().cmdloop()