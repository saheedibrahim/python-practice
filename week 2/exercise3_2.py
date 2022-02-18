def print_spam():
    print('spam')

def do_twice():
    print_spam()
    print_spam()

def do_four(print_spam, numb):
    do_twice()
    do_twice()

do_four(print_spam, 6)