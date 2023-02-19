n = 10
weight_limit = 100
weight_max = 0
items = [22, 22, 26, 26, 31, 31, 18, 18, 7, 7]

def _01_bag(i, weight_cur):
    if weight_cur == weight_limit or i == n:
        global weight_max
        if weight_cur > weight_max:
            weight_max = weight_cur
        return
    _01_bag(i+1, weight_cur)
    if items[i]+weight_cur <= weight_limit:
        _01_bag(i+1, items[i]+weight_cur)

_01_bag(0, 0)
print(weight_max)

