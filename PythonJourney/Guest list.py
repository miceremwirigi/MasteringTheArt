guests = ['Jackson', 'Eliud', 'Lenny']  # Create a list


def replace(sample, old, new):  # Replace element in a list
    print(sample)
    sample.remove(old)
    sample.append(new)
    pass


def insertintolist(sample, index, value):
    print('Inserting {} at index {}'.format(value, index))
    sample.insert(index, value)
    print(sample)


def sendinvite(sample):  # Use each element in the list in a sentence
    for i, index in enumerate(sample):
        print('Hi {}, you are invited for dinner'.format(sample[i]))


def sendapology(sample, available_seats):  # Remove a number of elements from the list
    while len(sample) > available_seats:
        removed_guest = sample.pop()
        print('Hi {}, dinner is canceled.Not enough seats.'.format(removed_guest))
    for i, index in enumerate(sample):
        print('Hi {}, you are still invited for dinner. '.format(sample[i]))
    print(sample)
    print()
    while len(sample) != 0:  # Remove all elements in the list
        print('Removing {}'.format(sample[len(sample) - 1]))
        del sample[len(sample) - 1]
        print(sample)


replace(guests, 'Lenny', 'John')

sendinvite(guests)
print()
insertintolist(guests, 0, 'Rose')
print()
insertintolist(guests, 2, 'Robert')
print()
sendinvite(guests)
print()
print(guests)
print()
sendapology(guests, 2)


