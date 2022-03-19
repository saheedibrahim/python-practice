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

# for c in test_dups:
    # d = has_duplicate(c)
    # if d:
        # print(f"{c} has duplicates")
    # else:
        # print(f"{c} has no duplicates")

def missing_letters(given):
    # letters = "abcdefghijklmnopqrstuvwxyz"
    missed = ""
    def givenLet(given):
        givenL = ""
        givenLetter = histogram(given)
        for d in givenLetter:
            givenL += d
        return givenL
    letters = histogram(alphabet)
    for c in letters:
        # for d in givenLetter:
        if c not in givenLet(given):
        # print(c)
        # f = 0
        # if c not in givenLetter:
            missed += c
                # print(missed)

            # f += 1
        else:
            missed = "all is available"
    # return missed
    # for c in sorted(givenLetter):
    # print(missingChar)
    # print(givenLetter)
    # print(letters)
        # if c not in letters:
            # missed += missed[c]
            # missed[c] = 1
            # print(missed)
# print(histogram('ghygfde'))
print(missing_letters('adert'))




def has_duplicate(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    if d[c] > 1:
        return True
    else:
        return False

alphabet = "abcdefghijklmnopqrstuvwxyzb"
print(has_duplicate(alphabet))