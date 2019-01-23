from coordinates import ground


territory = ground.Territory()
ploc = ground.Location(0, 2)



while True:
    answer=input("Enter Your direction >>> ").lower()
    if  answer in territory.check_possible_moves(ploc.current):
        ploc.move(answer)
    else:
        print
        continue
    territory.draw(ploc.current)


