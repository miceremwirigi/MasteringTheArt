
def doubleletters(letters):
    state = False
    i = 0
    while i < len(letters)-1:
        print('{} , {}'.format(letters[i], letters[i + 1]))
        if letters[i] == letters[i + 1]:
            state = True
            break
        i += 1
    return state


print(doubleletters('nana'))
