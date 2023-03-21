'''# naive solution
def consecutive_zeros(bin_str):
    result = 0
    streak = 0
    for letter in bin_str:
        if letter == "0":
            streak += 1
        else:
            streak = 0
        result = max(result, streak)
    return result

# shorter solution
def consecutive_zeros(bin_str):
    return max([len(s) for s in bin_str.split("1")])'''


def consecutive_zeros(s):
    n = 0
    m = 0
    for i, digit in enumerate(s):
        print(digit, '\t', n, '\t', m)
        if int(digit) == 0:
            n += 1
        if n > m:
            m = n
        elif int(digit) == 1:
            n = 0
    return m


print(consecutive_zeros("1001101000110"))
