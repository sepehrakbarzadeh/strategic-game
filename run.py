from coordinates import ground

territory = ground.Territory((5,5))
rand_location=territory.get_loc()
human_location=rand_location[0]
dragon_location=rand_location[1]

door_location=rand_location[2]


def check_lose():
    if human.distance(dragon_location) == 0 :
        print ("LOOOOOOOOOSE")
        return False
    return True

def check_win():
    if human.distance(door_location) == 0 :
        print ("WIIIIIIIN")
        return False
    return True

def clear():
    import os
    os.system('cls') if os.name=='nt' else os.system('clear')

def check_direction():
    allow_dir=['left','right','up','down','quit']
    while True:
        d=input('> ')
        if d  in allow_dir:
            break
    return d




human = ground.Location(human_location)

game_win=True
game_lose=True
while game_win and game_lose:
    clear()
    territory.draw(human.current)
    print(territory.check_possible_moves(human.current))
    print(human.current)
    print()
    print('dragon-- {}'.format(dragon_location))
    print('door-- {}'.format(door_location))
    direction=check_direction()
    if direction == 'quit':
        print('BYE')
        break
    human.move(direction)
    game_lose=check_lose()
    game_win=check_win()
