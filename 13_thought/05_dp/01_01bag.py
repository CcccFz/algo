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
    n = len(weights)
    dp = [False] * (weight_limit+1)
    prices_max = [0] * (weight_limit+1)
    dp[0], dp[weights[0]] = True, True
    prices_max[weights[0]] = prices[0]
    for i in range(1, n):
        for j in range(weight_limit-weights[i], -1, -1):
            if dp[j]:
                dp[j+weights[i]] = True
                prices_max[j+weights[i]] = max(prices_max[j+weights[i]], prices_max[j]+prices[i])
    price_max = 0
    for price in prices_max:
        if price > price_max:
            price_max = price
    return price_max

print(_01bag([2,2,4,6,3], 9)) # 9
print(_01bag_with_price([3, 2, 1, 1, 4], [5, 2, 4 ,2 ,10], 8)) # 19
