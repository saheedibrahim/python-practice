alphabet = "abcdefghijklmnopqrstuvwxyz"
test_dups = ['zzz', "dog", "bookkeeper", "subdermatoglyphic", "subdermatoglyphics"]
test_miss = ["zzz", "subdermatoglyphic", "the quick brown fox jumps over the lazy dog"]
testi = 'zzz'

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def has_duplicate(a):
    d = histogram(a)
    for c in d:
        if d[c] > 1:
            x = True
            break
        else:
            x = False
    return x

for c in test_dups:
    d = has_duplicate(c)
    if d:
        print(f"{c} has duplicates")
    else:
        print(f"{c} has no duplicates")

def missing_letters(t):
    d = histogram(t)
    for c in d:
        if c in alphabet:
            result = alphabet.replace(c, "")
        else:
            result = f"{alphabet} uses all the letters"
    return  result
print(missing_letters('abgt'))