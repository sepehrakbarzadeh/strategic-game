from coordinates import ground
from characters.thieves import Thief


thief = Thief(name = 'sepehr')

territory = ground.Territory()
ploc = ground.Location(3, 2)

territory.draw(ploc.current)

