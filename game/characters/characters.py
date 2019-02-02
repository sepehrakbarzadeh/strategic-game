
class Character:
    
    def __init__(self, name, *args, **kwargs):
        self.__name = name
        self.__hp = 150

        for key, value in kwargs.items():
            setattr(self, key, value)
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            if value.isalpha():
                self.__name = value
            else:
                raise ValueError("name must be alphabet.")
        else:
            raise TypeError("name must be string.")
    
    @name.deleter
    def name(self):
        self.__name = ""

    @property
    def hp(self):
        return self.__hp
    
    @hp.setter
    def hp(self, value):
        if isinstance(value, int):
            self.__hp += value

    @hp.deleter
    def hp(self):
        self.__hp = 0
    

    def __str__(self):
        return "{}: {}".format(self.__class__.__name__, self.name)

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.name)

