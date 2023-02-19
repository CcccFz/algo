# -*- coding: UTF-8 -*-
from typing import List

cap = 8
items_info = [(3, 5), (2, 2), (1, 4), (1, 2), (4, 10)]
picks = [0] * len(items_info)
max_price = 0
picks_max_price = [0] * len(items_info)


def _01_bag(items_info, picks, i, weight_cur):
    def get_value(items_info, picks):
        prices = [_[1] for _ in items_info]
        return sum(x*y for x, y in zip(picks, prices))

    if i == len(items_info) or weight_cur == cap:
        global max_price, picks_max_price
        if get_value(items_info, picks) > get_value(items_info, picks_max_price):
            picks_max_price = picks.copy()
            max_price = get_value(items_info, picks_max_price)
        return
    
    picks[i] = 1
    weight_item = items_info[i][0]
    if weight_item+weight_cur <= cap:
        _01_bag(items_info, picks, i+1, weight_cur+weight_item)

    picks[i] = 0
    _01_bag(items_info, picks, i+1, weight_cur)

if __name__ == '__main__':
    # (weight, price)
    
    _01_bag(items_info, picks, 0, 0)
    print(picks_max_price)
    print(max_price)