from codecs import lookup_error


values = {"a":2, "c":3, "b":1, "y":0}

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def reverse_loop(d, v):
    for k in d:
        if d[k] == v:
            return k
    # raise lookup_error('Value does not appear in the dictionary')

h = histogram('parrot')
print(reverse_loop(h, 1))