def _01bag(weights, weight_limit):
    states = [False] * (weight_limit+1)
    states[0], states[weights[0]] = True, True
    for i in range(1, len(weights)):
        for j in range(weight_limit-weights[i], -1, -1):
            if states[j]:
                states[j+weights[i]] = True
    for i in range(weight_limit, -1, -1):
        if states[i]:
            return i
    return 0

def _01bag_with_price(weights, prices, weight_limit):
    pass

print(_01bag([2,2,4,6,3], 9)) # 9
print(_01bag_with_price([3, 2, 1, 1, 4], [5, 2, 4 ,2 ,10], 8)) # 19
