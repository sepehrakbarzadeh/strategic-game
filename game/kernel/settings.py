from painless.pattern import Singleton

class Setting(metaclass = Singleton):
    LEVELS = ('easy', 'normal', 'hard')

    def __init__(self, level, *args, **kwargs):
        self.level = level

    
    @property
    def level(self):
        return self.__level
    
    @level.setter
    def level(self, value):
        if isinstance(value, str):
            if value in self.LEVELS:
                self.__level = value
            else:
                raise ValueError("you must choose one of these levels: {}".format(', '.join(self.LEVELS)))
        else:
            raise TypeError("value must be str.")


    @staticmethod
    def clear_screen():
        from os import system, name
        system('cls' if name == 'nt' else 'clear')
