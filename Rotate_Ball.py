

def rotate_ball(n, k):
    mapping = {}
    ex_set = set()
    for _ in range(n):
        t = raw_input().split(' ')
        exchange = (t[0], t[1]) if t[0] > t[1] else (t[1], t[0])
        if exchange in ex_set:
            ex_set.remove(exchange)
        else:
            ex_set.add(exchange)

    



if __name__ == 'main':
