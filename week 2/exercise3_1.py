def right_justify(monty):
    len_arg = len(monty)
    s = ' ' * (70 - len_arg) + monty
    print(s)
    print(len_arg)
    print(len(s))

right_justify('ass')
right_justify('school')
right_justify('modrosah')