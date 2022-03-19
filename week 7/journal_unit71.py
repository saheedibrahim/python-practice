def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

fruits = {'apple': 3, 'banana':2, 'orange':2}
print(fruits)
print(invert_dict(fruits))