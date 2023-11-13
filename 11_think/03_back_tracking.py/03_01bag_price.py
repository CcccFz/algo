# -*- coding: UTF-8 -*-

cap = 8
items = [(3, 5), (2, 2), (1, 4), (1, 2), (4, 10)]
picks = [False] * len(items)
picks_max_price = [False] * len(items)
price_max = 0

def _01_bag(i, weight_cur):
    global price_max, picks_max_price

    def get_price(items, picks):
        return sum([item[1] for i, item in enumerate(items) if picks[i]])
    
    if weight_cur == cap or i == len(items):
        if get_price(items, picks) > get_price(items, picks_max_price):
            picks_max_price = picks.copy()
            price_max = get_price(items, picks_max_price)
        return
    
    picks[i] = False
    _01_bag(i+1, weight_cur)

    picks[i] = True
    if weight_cur+items[i][0] <= cap:
        _01_bag(i+1, weight_cur+items[i][0])

if __name__ == '__main__':
    # (weight, price)
    
    _01_bag(0, 0)
    print(picks_max_price)
    print(price_max)