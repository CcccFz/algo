weights = [3, 2, 1, 1, 4]
prices = [5, 2, 4, 2, 10]
weight_limit = 8
n = len(weights)

picks = [False] * n
picks_max_price = [False] * n
price_max = 0

def _01_bag(i, weight_cur, price_cur):
    global price_max, picks_max_price
    
    if weight_cur == weight_limit or i == n:
        if price_cur > price_max:
            price_max = price_cur
            picks_max_price = picks.copy()
        return
    
    picks[i] = False
    _01_bag(i+1, weight_cur, price_cur)

    picks[i] = True
    if weight_cur+weights[i] <= weight_limit:
        _01_bag(i+1, weight_cur+weights[i], price_cur+prices[i])

    
_01_bag(0, 0, 0)
print(picks_max_price)
print(price_max)