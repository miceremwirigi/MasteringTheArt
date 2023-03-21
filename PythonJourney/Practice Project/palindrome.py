def palindrome(s):
    x = len(s)
    i = 0
    #print(s[2]==s[3])
    while i <  len(s)/2:
        if s[i] !=  s[len(s)-1-i]:
            is_palindrome = False
            return is_palindrome
        else:
            is_palindrome = True    
        i += 1
    return is_palindrome


print(palindrome('bob'))
