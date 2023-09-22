def _01bag(items, weight_limit):
    states = [False] * (weight_limit+1)
    states[0], states[items[0]] = True, True
    for i in range(1, len(items)):
        for j in range(weight_limit-items[i], -1, -1):
            if states[j]:
                states[j+items[i]] = True

    for j in range(weight_limit, -1, -1):
        if states[j]:
            return j
    return 0

def _01bag_with_price(items, weight_limit):
    states = [-1] * (weight_limit+1)
    states[0], states[items[0][0]] = 0, items[0][1]
    for i in range(1, len(items)):
        for j in range(weight_limit-items[i][0], -1, -1):
            if states[j] >= 0:
                if states[j+items[i][0]] < states[j]+items[i][1]:
                    states[j+items[i][0]] = states[j]+items[i][1]
    
    max_price = 0
    for price in states:
        if price > max_price:
            max_price = price
    return max_price

print(_01bag([2,2,4,6,3], 9)) # 9
print(_01bag_with_price([(3,5),(2,2),(1,4),(1,2),(4,10)], 8)) # 19