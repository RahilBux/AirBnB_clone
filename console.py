#!/usr/bin/python3
"""Module for the console programme"""
import cmd
from models.base_model import BaseModel
from models import storage
import re
import json


class HBNBCommand(cmd.Cmd):
    """Class for the command line interpreter"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """End Of Line character handled"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """For an empty line does nothing"""
        pass

    def do_create(self, line):
        """Creates an instance of model"""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            new = storage.classes()[line]()
            new.save()
            print(new.id)

    def do_show(self, line):
        """Prints the string rep of an instance"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            word = line.split(' ')
            if word[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(word) < 2:
                print("** instance id missing **")
            else:
                k = "{}.{}".format(word[0], word[1])
                if k not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[k])

    def do_destroy(self, line):
        """Deletes an instance based on name and ID"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            word = line.split(' ')
            if word[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(word) < 2:
                print("** instance id missing **")
            else:
                k = "{}.{}".format(word[0], word[1])
                if k not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[k]
                    storage.save()

    def do_all(self, line):
        """print all str repr of all instances"""
        if line != "":
            word = line.split(' ')
            if word[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                new1 = [str(val) for key, val in storage.all().items()
                        if type(val).__name__ == word[0]]
                print(new1)
        else:
            list_new = [str(val) for key, val in storage.all().items()]
            print(list_new)

    def do_update(self, line):
        """Updates an instance by changing or adding attributes"""
        if line == "" or line is None:
            print("** class name missing **")
            return

        regex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(regex, line)
        class_name = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        val = match.group(4)
        if not match:
            print("** class name missing **")
        elif class_name not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            k = "{}.{}".format(class_name, uid)
            if k not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not val:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', val):
                    if '.' in val:
                        cast = float
                    else:
                        cast = int
                else:
                    val = val.replace('"', '')
                attributes = storage.attributes()[class_name]
                if attribute in attributes:
                    val = attributes[attribute](val)
                elif cast:
                    try:
                        val = cast(value)
                    except ValueError:
                        pass
                setattr(storage.all()[k], attribute, val)
                storage.all()[k].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
