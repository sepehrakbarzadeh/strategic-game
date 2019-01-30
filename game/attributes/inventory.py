class Inventory:
    
    def __init__(self, *args, **kwargs):
        self.slots = list()

    def add(self, item):
        self.slots.append(item)

    def __len__(self):
        return len(self.slots)
    
    def __contains__(self, item):
        return item in self.slots
    
    def __iter__(self):
        yield from self.slots
