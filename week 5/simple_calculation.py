inputValue = input()
def eval_loop(inputValue):
    while True:
        result = eval(inputValue)
        if inputValue == 'done':
            break
        inputValue = input()
        print(result)

eval_loop(input())