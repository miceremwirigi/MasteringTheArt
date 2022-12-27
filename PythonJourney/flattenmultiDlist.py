'''Write a function that takes a list of lists and flattens it into a one-dimensional list.

Name your function flatten. It should take a single parameter and return a list.


# naive solution
def flatten(outer_list):
    result = []
    for inner_list in outer_list:
        for item in inner_list:
            result.append(item)
    return result

# solution with nested list comprehensions
# (can be put on a single line for conciseness)
def flatten(outer_list):
    return [
        item
        for inner_list in outer_list
        for item in inner_list
    ]
    '''


def flatten(list):
    new_list = []
    i = 0
    j = 0
    while i < len(list):
        j = list[i]
        for k in j:
            new_list.append(k)
        i += 1
    return new_list


list1 = [[1, 2], [3, 4]]
print(flatten(list1))
