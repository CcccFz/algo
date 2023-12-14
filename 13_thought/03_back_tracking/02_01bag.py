weights = [22, 22, 26, 26, 31, 31, 18, 18, 7, 7]
n = len(weights)
weight_limit = 100
weight_max = 0

# mem = [[False] * (weight_limit+1)] * n

def _01_bag(i, weight_cur):
    global weight_max, weight_max
    if weight_cur == weight_limit or i == n:
        if weight_cur > weight_max:
            weight_max = weight_cur
        return
    # if mem[i][weight_cur]:
    #     return
    # mem[i][weight_cur] = True
    _01_bag(i+1, weight_cur)
    if weight_cur+weights[i] <= weight_limit:
        _01_bag(i+1, weight_cur+weights[i])

_01_bag(0, 0)
print(weight_max)