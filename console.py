#!/usr/bin/python3
# console.py

import re  # Import the regular expressions module
from models.base_model import BaseModel
from models import storage

# ...

class HBNBCommand(cmd.Cmd):
    # ...

    def do_create(self, arg):
        """Create a new instance of a given class."""

        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        # Parse command arguments and create a dictionary with key-value pairs
        attributes = {}
        pattern = re.compile(r'(\w+)="?(.*?)"?$')  # Regular expression pattern to match key-value pairs
        for arg in args[1:]:
            match = pattern.match(arg)
            if match:
                key, value = match.groups()
                value = value.replace("_", " ")
                try:
                    value = int(value)
                except ValueError:
                    try:
                        value = float(value)
                    except ValueError:
                        pass
                attributes[key] = value

        # Create an object using the attributes dictionary
        obj = HBNBCommand.classes[args[0]](**attributes)  # Create a new instance of the class with the attributes
        obj.save()  # Call the save method to persist the object
        print(obj.id)  # Print the id of the newly created object
