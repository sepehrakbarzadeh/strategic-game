from .characters import Character

from game.attributes.agility import Agile, Sneaky
from game.attributes.strength import Gient

class Human(Sneaky, Agile, Character):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hp += 1500 
    
    def walk(self):
        print("Human is walking..")


class Dragon(Gient, Character):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hp += 4950
    
    def shout(self):
        print("The Dragon is shouting")


class HeroFactory:

    @classmethod
    def __get_characters(self):        
        from ast import parse, ClassDef
        from inspect import getfile, currentframe
        

        file_name = getfile(currentframe())
        with open(file_name, 'r') as file:
            node = parse(file.read())
        
        classes = [n.name for n in node.body if isinstance(n, ClassDef)]
        return classes

    @classmethod
    def create(cls, character):
        for class_name in cls.__get_characters():
            if character == class_name:
                return eval(class_name)

            
