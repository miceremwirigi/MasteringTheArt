'''def up_down(x):
    return (x-1, x+1)'''

def up_down(n):
    n = int (n)
    mylist = [n-1, n+1]
    return tuple(mylist)

print(up_down(5))