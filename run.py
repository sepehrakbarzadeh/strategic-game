from coordinates import ground
from characters.hero import Human, Dragon

# territory = ground.Territory()
# ploc = ground.Location(3, 2)

# territory.draw(ploc.current)


player = Human(name = 'sepehr')
dragon = Dragon(name = 'demon')

player.walk()
dragon.shout()

