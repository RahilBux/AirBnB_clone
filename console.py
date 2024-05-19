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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
