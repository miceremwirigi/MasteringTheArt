size = 10

def main():
    for i in range(1,7):
        drawDiamondOutline(i)
        print()
        drawDiamondFilled(i)
        print()


def drawDiamondOutline(size):
    for i in range(size):
        print(' ' * (size - i), end='')
        print('/', end='')
        print(' ' * 2*i, end='')
        print('\\')
    for i in range(size):
        print(' ' * (i + 1), end='')
        print('\\',end='')
        print(' ' * (size - i -1) * 2, end='')
        print('/')


def drawDiamondFilled(size):
    for i in range(size):
        print(' ' * (size - i), end='')
        print('/' * i, end='')
        print('\\' * i)
        # print('\\')
    for i in range(size):
        print(' ' * (i + 1), end='')
        print('\\' * (size - i - 1), end='')
        print('/' * (size - i - 1))
        # print('/')


if __name__ == "__main__":
    main()
