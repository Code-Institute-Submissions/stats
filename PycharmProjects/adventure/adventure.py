from data import locations
def got_to(directions, position):
        direction_error = directions
        position_error = position
        location = locations[position]
        print('you are at the %s' % location)

        valid_directions = {}
        for k, v in directions.items():
            possible_position = (position[0] + v[0], position[1] + v[1])
            possible_location = locations.get(possible_position)
            if possible_location:
                print('to the %s is a %s' % (k, possible_location))
                valid_directions[k] = possible_position

        direction = input('which direction do you wanna go\n')
        try:
            position = valid_directions[direction]
            got_to(directions, position)
        except KeyError:
            print('invalid location entered! Try again\n')
            got_to(direction_error, position_error)

def play():
    directions = {
        'west': (-1, 0),
        'east': (1, 0),
        'north': (0, -1),
        'south': (0, 1),
    }
    position = (0, 0)
    got_to(directions, position)

play()




