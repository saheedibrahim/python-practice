"""A chained conditional statement is a statement that uses a if, elif
 and else statement in each branch without one branch having another 
 conditional statement like if, elif or else WHILE a nested conditional
 statement uses another conditional statement in a conditional statement.
 That means that in a nested conditional statement we can have an if
statement inside another if statement.
Nested conditional statement is usually hard to read compared to chained 
conditional sttatement.
"""

def chained_conditional(x):
    if 0 <= x <= 9:
        print(x, ' is a number between 0 to 9, 0 and 9 are inclusive.')
    elif 10 <= x <= 99:
        print(x, ' ranges between 10 to 99, 10 and 99 are inclusive.')
    else:
        print(x, ' is either negative or greater than 99')

chained_conditional(9)


def nested_conditional(x):
    if 0 <= x <= 9:
        print(x, ' is a number between 0 to 9, 0 and 9 are inclusive.')
    else:
        if 10 <= x <= 99:
            print(x, ' ranges between 10 to 99, 10 and 99 are inclusive.')
        else:
            print(x, ' is either negative or greater than 99')

nested_conditional(-9)

""""using logical operator simplifies nested conditional"""

def deeply_nested_conditional(x):
    if 10 < x:
        if x % 2 == 0:
            if x < 100:
                print(x, ' is an even number between 10 to 100')

deeply_nested_conditional(98)

def single_nested_conditional(x):
    if 10 < x < 100 and x % 2 == 0:
        print(x, ' is an even number between 10 to 100')

single_nested_conditional(48)
