#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command line interpreter for HBNB project"""
    prompt = "(hbnb) "

    
    def do_create(self, arg):
        """Create a new instance of a class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(args[0])()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    
    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            try:
                print(storage.all()[key])
            except KeyError:
                print("** no instance found **")

    
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            try:
                del storage.all()[key]
                storage.save()
            except KeyError:
                print("** no instance found **")

    
    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        if len(args) == 0:
            print([str(obj) for obj in storage.all().values()])
        else:
            try:
                cls_name = args[0]
                print([str(obj) for obj in storage.all().values()
                       if type(obj).__name__ == cls_name])
            except NameError:
                print("** class doesn't exist **")

    
    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            try:
                obj = storage.all()[key]
                setattr(obj, args[2], args[3])
                obj.save()
            except KeyError:
                print("** no instance found **")

    
    def do_EOF(self, arg):
        """Handles end of file"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Handles empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
