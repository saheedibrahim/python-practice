def endless_loop(n):
    if n <= 0:
        print(n)
    else:
        print(f'counting from {n} to ...')
        endless_loop(n + 1)

endless_loop(4)