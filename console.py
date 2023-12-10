#!/usr/bin/python3

'''The cmd Module. 
This is an interface that will enable interaction with the software'''

import cmd
from models.base_model import BaseModel
from models import storage
import re
from datetime import datetime

class HBNBCommand(cmd.Cmd):
    '''This is the main class for the module.'''

    prompt = "(hbnb) "
    
    
     CLASSES = {
        'BaseModel': BaseModel,
        #'User': User,
        #'State': State,
        #'City': City,
        #'Amenity': Amenity,
        #'Place': Place,
        #'Review': Review
    }

    def emptyline(self):
        '''Nothing will be executed if an empty line is passed.'''
        pass

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, line):
        '''This will quit the program'''
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel and saves it to json file"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            obj = self.CLASSES[class_name]()
            obj.save()
            print(obj.id)
        except ImportError:
            print("** class doesn't exist **")
    
    def do_show(self, line):
        """Prints the string representation of an instance"""
        args = line.split()
        if not args:
            print("** class name missing **")
        
        cls_name = args[0]
        elif cls_name not in self.CLASSES:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{cls_name}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, line)
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)."""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.CLASSES:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()
    
    def do_all(self, line):
            """Prints all string representation of all instances based
            or not on the class name."""
            args = line.split()


            if not args:
                print([str(obj) for obj in storage.all().values()])
            elif args[0] not in self.CLASSES:
                print("** class doesn't exist **")
            else:
                cls_name = args[0]
                instance = [
                    str(obj) for key in storage.all().items()
                    if key.startswith(cls_name + '.')
                ]
                print(instance)
            
    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        """
        args = line.split()
        
        if not args:
            print("** class name missing **")
            return
        
        

if __name__ == "__main__":
    HBNBCommand().cmdloop()