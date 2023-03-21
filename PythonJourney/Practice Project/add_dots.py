def add_dots(letters):
    newString = ""
    i = 0
    while i < len(letters):
        if i < len(letters)-1:
            newString = newString + letters[i] + '.'
        else:
            newString = newString + letters[i]
        i += 1
    return newString


def remove_dots(letters):
    newString = letters.replace('.', '')
    return newString


print(remove_dots(add_dots('abc')))


'''# the longer way
def add_dots(s):
    out = ""
    for letter in s:
        out += letter + "."
    return out[:-1]

def remove_dots(s):
    out = ""
    for letter in s:
        if letter != ".":
            out += letter
    return out


# the short way
def add_dots(s):
    return ".".join(s)

def remove_dots(s):
    return s.replace(".", "")'''
