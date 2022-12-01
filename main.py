def spiral(size):
    """ 
        The square spiral (rows = columns)
        The spiral should start on the top left most cell 
        each edge should be one unit shorter as the spiral winds around and finally ends
        Example: spiral 5
            [* * * * *]
            [        *]
            [    *   *]
            [    * * *]
            [         ]
    """
    #Initial a spiral of grid size * size
    columns = size
    rows = size
    grid = []
    sym = '* '
    for _ in range(rows):
        col = []
        for x in range(columns + 2):
            if x == 0:
                col.append('[')
            elif x == columns + 1:
                col.append(']')
            else:
                col.append('  ')
        grid.append(col)
    start_position = (0, 1)
        
    # Change value of the grid to create the spiral
    # The spiral should start on the top left most cell 

    current_position = start_position
    steps = number_steps(columns)

    grid[get_y(current_position)][get_x(current_position)] = sym
    steps -= 1
    current_dir = "right"
    side = columns - 1
    while steps > 0:
        for _ in range(side):
            current_position = change_position(current_dir, current_position)
            grid[get_y(current_position)][get_x(current_position)] = sym
        steps -= side
        side -= 1
        current_dir = change_direction(current_dir)
    
    # print out a spiral of user input's size
    print_spiral(grid, size)
    
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

def print_spiral(grid, size):
        """ Printing spiral to console
        """
        for y in range(0, size):
            for x in range(0, size + 2):
                print(grid[y][x], end="")
            print('\n', end="")

if __name__ == '__main__':
    user_input = input("Please enter a positive number size for spiral: ")
    while input_validation(user_input) is not True:
        user_input = input("Please enter a positive number size for spiral: ")
    size = int(user_input)
    spiral(size)