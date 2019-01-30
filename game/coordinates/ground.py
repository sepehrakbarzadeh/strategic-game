from math import hypot
import random

class Location:
    DIRECTIONS = ('right', 'left', 'up', 'down')

    def __init__(self, x_axis = 0, y_axis = 0):
        """Defines x and y variables
        
        Arguments:
            x {[int]} -- [x coordinate]
            y {[int]} -- [y coordinate]
        """
        if x_axis < 0 or y_axis < 0:
            raise ValueError("Value must be positive")

        self.X = x_axis
        self.Y = y_axis
        self.vector = (x_axis, y_axis)

    def travel(self, dx, dy):
        """Determines where x and y move
        
        Arguments:
            dx {[int]} -- [Determine move forward on the x-axis.]
            dy {[int]} -- [Determine move forward on the y-axis.]
        """
        self.X += dx
        self.Y += dy

        return self.current
    
    def move(self, direction):
        right, left, up, down = self.DIRECTIONS        
        direction = direction.lower()

        if not direction in self.DIRECTIONS:
            raise ValueError("You must enter one of these values {}".format(direction))

        if direction == right:
            self.X + 1
        if direction == left:
            self.X -= 1
        if direction == up:
            self.Y += 1
        if direction == down:
            self.Y -= 1
        
        return self.current

    def distance(self, pos):
        dx = pos.X - self.X
        dy = pos.Y - self.Y
        return hypot(dx, dy)
    
    @property
    def current(self):
        return self.X, self.Y

    @property
    def getX(self):
        return self.X
    
    def setX(self, value):
        self.X = value
    
    @property
    def getY(self):
        return self.Y
    
    def setY(self, value):
        self.Y = value

    def __add__(self, other):
        """ Returns the vector addition of self and other """
        return Location(*(a + b for a, b in zip(self.vector, other.vector)))
    
    def __iadd__(self, other):
        return Location(*(a + b for a, b in zip(self.vector, other.vector)))

    def __sub__(self, other):
        """ Returns the vector addition of self and other """
        return Location(*(a - b for a, b in zip(self.vector, other.vector)))
    
    def __str__(self):
        return "Point({}, {})".format(self.X, self.Y)


# Suggestions
## Region
## Territory
## Grid
class Territory:
    def __init__(self, dimension = (10, 10), *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cells = [(x, y) for y in range(dimension[1]) for x in range(dimension[0])]
        self.boundries = (dimension[0], dimension[1])
    
    def draw(self, ploc):
        """draw a grid with set dimension.
        
        Arguments:
            ploc {[tuple]} -- [The location of the user]
        """
        # import pdb; pdb.set_trace()
        print(" _" * self.boundries[0])
        tile = "|{}"

        for cell in self.cells:
            x, y = cell
            if x < self.boundries[0] - 1:
                line_end = ""
                if cell == ploc:
                    output = tile.format("X")
                else:
                    output = tile.format("_")
            else:
                line_end = "\n"
                if cell == ploc:
                    output = tile.format("X|")
                else:
                    output = tile.format("_|")
            
            print(output, end=line_end)

    def get_loc(self):
        return random.sample(self.cells, 3)

    def check_possible_moves(self, ploc):
        possible_moves = ['left', 'right', 'up', 'down']
        
        x, y = ploc
        
        if x == 0:
            possible_moves.remove("left")
        if x == self.boundries[0]:
            possible_moves.remove('right')
        if y == 0:
            possible_moves.remove('up')
        if y == self.boundries[1]:
            possible_moves.remove('down')
        
        return possible_moves

    def move_player(self, ploc, movement):
        x, y = ploc
        movement = movement.lower()
        
        if movement == "left":
            x -= 1
        if movement == "right":
            x += 1
        if movement == "up":
            y -= 1
        if movement == "down":
            y += 1
    
        return x, y
    
        







    