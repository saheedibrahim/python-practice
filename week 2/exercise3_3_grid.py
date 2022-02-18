def straight():
    print('|', '  ' * 4, '|', '  ' * 4, ' |', '  ' * 4, '|', '  ' * 4, ' |')
    print('|', '  ' * 4, '|', '  ' * 4, ' |', '  ' * 4, '|', '  ' * 4, ' |')
    print('|', '  ' * 4, '|', '  ' * 4, ' |', '  ' * 4, '|', '  ' * 4, ' |')
    print('|', '  ' * 4, '|', '  ' * 4, ' |', '  ' * 4, '|', '  ' * 4, ' |')

def top():
    print('+', ' -' * 4, '+', ' -' * 4, ' +', ' -' * 4, '+', ' -' * 4, ' +')

def two_sides():
    straight()
    top()

def grid():
    top()
    two_sides()
    two_sides()
    two_sides()
    two_sides()

grid()