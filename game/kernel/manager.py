from .settings import Setting
from game.coordinates.ground import Territory
from game.coordinates.ground import Location
from game.characters.hero import HeroFactory



def run(level, users = 10):
    setting = Setting(level)
    territory = Territory()
    ploc = Location(3, 2)
    
    players = list()


    players = [ 
        player(name='user{}'.format(i))
        for i in range(users)
            for player in [HeroFactory.create('Human')]
    ]
    
    print("game is running...")
    print("below players are playing:")
    for player in players:
        print(player)

    # territory.draw(ploc)
    print("game END...")
    
    