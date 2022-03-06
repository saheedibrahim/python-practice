def greaterNumber(value):
    bigNumber = []
    for n in value:
        s = int(n)
        if s > 4:
            bigNumber.append(n)
    return bigNumber

print(greaterNumber('254387'))
mylist = ["now", "four", "is", "score", "the", "and seven", "time", "years", "for"]
print(" ".join(mylist[1::2]))