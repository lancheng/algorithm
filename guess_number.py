def guess(n):
    if n < 6:
        return -1
    if n > 6:
        return 1

    return 0

def guess_number(n):
    s = 1
    e = n
    while s <= e:
        m = s + (e - s) / 2
        guess_result = guess(m)
        if guess_result == -1:
            s = m + 1
        elif guess_result == 1:
            e = m - 1
        else:
            return m

if __name__ == '__main__':
    print guess_number(10)