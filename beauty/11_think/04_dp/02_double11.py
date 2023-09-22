def double11(items, least):
    states = [False] * (2*least+1)
    states[0], states[items[0]] = True, True
    for i in range(1, len(items)):
        for j in range(2*least-items[i], -1, -1):
            if states[j]:
                states[j+items[i]] = True
    
    price = -1
    for j in range(least, 2*least+1):
        if states[j]:
            price = j
            break
    picks = []
    _price = price
    for i in range(len(items)-1, -1, -1):
        if _price > 0 and states[_price-items[i]]:
            picks.insert(0, items[i])
            _price -= items[i]

    return price, picks


if __name__ == '__main__':
    print(double11([10,20,30,20,70,60,40,30,40,10,20], 200))
    print(double11([33,73,13,53,13,13,23,43,83,73,83], 200))