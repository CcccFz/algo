items = [22, 22, 26, 26, 31, 31, 18, 18, 7, 7]
n = len(items)
weight_limit = 100
weight_max = 0

def _01_bag(i, weight_cur):
    global weight_max, weight_max
    if weight_cur == weight_limit or i == n:
        if weight_cur > weight_max:
            weight_max = weight_cur
        return
    _01_bag(i+1, weight_cur)
    if weight_cur+items[i] <= weight_limit:
        _01_bag(i+1, weight_cur+items[i])

_01_bag(0, 0)
print(weight_max)

