***REMOVED*** ***REMOVED***:
    """ The square spiral (rows = columns)
        The spiral should start on the top left most cell 
        each edge should be one unit shorter as the spiral winds around and finally ends
        Example: spiral 5
            [* * * * *]
            [        *]
            [    *   *]
            [    * * *]
            [         ]
    """
    def __init__(self, size):
        """ ***REMOVED***ial a spiral of grid size * size
        """
        self.columns = size
        self.rows = size
        self.grid = []
        self.sym = '* '
        for _ in range(self.rows):
            col = []
            for x in range(self.columns + 2):
                if x == 0:
                    col.append('[')
                elif x == self.columns + 1:
                    col.append(']')
                else:
                    col.append('  ')
            self.grid.append(col)
        self.start_position = (0, 1)
        

    def create(self):
        """ Change value of the grid to create the spiral
            The spiral should start on the top left most cell 
        """
        #for y in range(self.rows):
        #    for x in range(1, self.columns + 1, 1):
        current_position = self.start_position
        steps = number_steps(self.columns)

        self.grid[get_y(current_position)][get_x(current_position)] = self.sym
        steps -= 1
        current_dir = "right"
        side = self.columns - 1
        while steps > 0:
            for _ in range(side):
                current_position = change_position(current_dir, current_position)
                self.grid[get_y(current_position)][get_x(current_position)] = self.sym
            steps -= side
            side -= 1
            current_dir = change_direction(current_dir)
    
    def print_spiral(self):
        """ Printing spiral to console
        """
        for y in range(0, self.rows):
            for x in range(0, self.columns + 2):
                print(self.grid[y][x], end="")
            print('\n', end="")

###########################
# Helpers Functions
###########################
def number_steps(size):
    """ Calculate numbers of '*'
    """
    steps = 1
    size -= 1
    while size >= 1:
        steps += size
        size -= 1
    return steps

def move_right(y, x):
    """ Calculate next position when move right from (y, x)
    """
    return y, x + 1

def move_left(y, x):
    """ Calculate next position when move left from (y, x)
    """
    return y, x - 1

def move_down(y, x):
    """ Calculate next position when move down from (y, x)
    """
    return y - 1, x

def move_up(y, x):
    """ Calculate next position when move up from (y, x)
    """
    return y + 1, x

def change_direction(dir):
    """ return string of next direction to move
    """
    if dir == "right":
        return "up"
    elif dir == "down":
        return "right"
    elif dir == "left":
        return "down"
    else:
        return "left"

def change_position(dir, position):
    """ return tupple of next position based on current direction
    """
    y = get_y(position)
    x = get_x(position)
    if dir == "right":
        return move_right(y, x)
    elif dir == "down":
        return move_down(y, x)
    elif dir == "left":
        return move_left(y, x)
    else:
        return move_up(y, x)

def get_y(position):
    """ Position is a tuple of (y, x)
    """
    return position[0]
    
def get_x(position):
    """ Position is a tuple of (y, x)
    """
    return position[1]

def input_validation(user_input):
    """ input need to be positive integer larger than
    """
    try:
        int(user_input)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    user_input = input("Please enter a positive number size for spiral: ")
    while input_validation(user_input) is not True:
        user_input = input("Please enter a positive number size for spiral: ")
    size = int(user_input)
    x = ***REMOVED***(size)
    x.create()
    x.print_spiral()