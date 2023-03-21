'''calling get_row_col("A3") should return the tuple (2, 0) 
because A3 corresponds to the row at index 2 and column at 
index 0in the board.'''


def get_row_col(a):
    a = set(a)
    b = map(dict([('A', 0), ('B', 1), ('C', 2),
            ('1', 0), ('2', 1), ('3', 2)]).get, a)
    return tuple(b)

#string = "hello"

#t = tuple(string)

# print(t)
