"""Object-oriented programming practice 1"""


#   Class
class Employees:
    memberStatus = "Employed"  # Class attributes

    def __init__(self, name, level, age):
        self.name = name  # Instance attributes
        self.level = level  #
        self.age = age


#  Instance
emp1 = Employees("Mike", "Junior", 23)
emp2 = Employees("Lucy", "Senior", 29)


class Businessmen:
    memberStatus = "Self employed"

    def __int__(self, name, level, age):
        self.name = name
        self.level = level
        self.age = age


# bsMan1 = Businessmen("Lloyd", "Senior", 34)
# bsMan2 = Businessmen("Claire", "Junior", 26)

print(emp1.name)
