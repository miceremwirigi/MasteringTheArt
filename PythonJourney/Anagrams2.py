def get_largest_anagram(list):
    list_copy = list[:]  # Make a copy of list to avoid changing list
    largest_anagram = []  # stores largest number of words with the same letters, i.e., anagrams
    anagram_count = 0  
    
    for word in list_copy:
        ref_string = word  # Pick a reference word in the list to copare with the rest
        anagram_list = []  # List to store anagrams temporarily
        
        for word in list_copy:  # Check for anagrams to each reference word
            if sorted(ref_string) == sorted(word):  
                anagram_list.append(word)

        if len(anagram_list) > anagram_count:  # Pick the most words with similar letters, i.e, largest anagram
            largest_anagram = anagram_list[:]
            anagram_count = len(anagram_list)
            

    print(largest_anagram)  
    return len(largest_anagram)  # return the size of the largest subset of equivalent words


print(get_largest_anagram(['cats', 'caller', 'dogs', 'cellar', 'parrots', 'recall']))