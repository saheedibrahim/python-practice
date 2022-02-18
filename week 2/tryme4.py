def new_line():
    print('.')

def three_lines():              #produces 3 lines of dots
    new_line()
    new_line()
    new_line()

def nine_lines():               #produce 9 lines of dots
    three_lines()
    three_lines()
    three_lines()

def clear_screen():             #produces 25 lines of dots.
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()
    new_line()

nine_lines()
print('Calling clearScreen')    #used to space between the 9lines and the clear screen
clear_screen()
