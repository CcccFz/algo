def double11(prices, least):
    states = [False] * (2*least+1)
    states[0], states[prices[0]] = True, True
    for i in range(1, len(prices)):
        for j in range(2*least-prices[i], -1, -1):
            if states[j]:
                states[j+prices[i]] = True

    price = 0
    for i in range(least, 2*least+1):
        if states[i]:
            price = i
            break

    _price = price
    picks = []
    # TODO: 该方法是错误的，有问题
    for i in range(len(prices)-1, -1, -1):
        if _price == 0:
            break
        if _price >= prices[i] and states[_price-prices[i]]:
            _price -= prices[i]
            picks.insert(0, prices[i])

    return price, picks


# (200, [60, 40, 30, 40, 10, 20])
print(double11([10, 20, 30, 20, 70, 60, 40, 30, 40, 10, 20], 200))

# (202, [23, 73, 83])
print(double11([33, 73, 13, 53, 13, 13, 23, 43, 83, 73, 83], 200))
