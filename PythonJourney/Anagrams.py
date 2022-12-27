def get_largest_anagram(list):
    list_copy = list[:]  # Make a copy of list to avoid changing list
    # stores largest number of words with the same letters, i.e., anagrams
    largest_anagram = []
    anagram_count = 0

    for word in list_copy:
        ref_string = word  # Pick a reference word in the list to copare with the rest
        anagram_list = []  # List to store anagrams temporarily

        for word in list_copy:  # Check for anagrams to each reference word
            if sorted(ref_string) == sorted(word):
                anagram_list.append(word)

        # Pick the most words with similar letters, i.e, largest anagram
        if len(anagram_list) > anagram_count:
            largest_anagram = anagram_list[:]
            anagram_count = len(anagram_list)

    #print(largest_anagram)
    # return the size of the largest subset of equivalent words
    return len(largest_anagram)


def main():
    list = []
    list_length = int(input(
        'How many words do we check for anagrams?\n(Enter number: '))

    while len(list) < list_length:
        word = input('Enter word number {}: '.format(len(list)+1))
        list.append(word)

    print(get_largest_anagram(list))
    

main()
# print(get_largest_anagram(
#    ['cats', 'caller', 'dogs', 'cellar', 'parrots', 'recall']))
