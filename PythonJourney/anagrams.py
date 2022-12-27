'''# easy solution
def is_anagram(string1, string2):
    return sorted(string1) == sorted(string2)

# harder solution:
# count how many times each letter appears in each string,
# and make sure all the counts are the same.
def count_letters(string):
    return {l: string.count(l) for l in string}
def is_anagram(string1, string2):
    return count_letters(string1) == count_letters(string2)'''


def is_anagram(word1, word2):
    list1 = []
    list2 = []
    for i,word in enumerate(word1):
        list1.append(word)
    print(list1)
    for i, word in enumerate(word2):
        list2.append(word)
    print(list2)
    for a in list1:
        if a in list2:
            state = True
        else:
            state = False
            return state
        list1.remove(a)
        list2.remove(a)
    for a in list2:
        if a in list1:
            state = True
        else:
            state = False
    return state

print(is_anagram('test','tess'))