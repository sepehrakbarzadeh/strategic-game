from .characters import Character
from attributes.agility import Agile, Sneaky
from attributes.strength import Gient

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
    