def convert(ints):
    return [str(x) for x in ints]


print(convert([1, 2, 3]))


'''# using a list comprehension
def convert(ns):
    return [str(n) for n in ns]

# using map
def convert(ns):
    return list(map(str, ns))'''
