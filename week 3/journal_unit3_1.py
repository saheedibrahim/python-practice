def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n - 1)

def countup(n):
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n + 1)

def select_count(n):
    if n <= 0:
        print(f'The output from {n} to zero is ...')
        countup(n)
    else:
        print(f'The output from {n} to zero is ...')
        countdown(n)

prompt = input("write a number...\n")
select_count(int(prompt))