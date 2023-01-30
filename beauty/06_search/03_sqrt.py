def my_sqrt(x):
    left, right = 0, x
    while left <= right:
        mid = (left + right) / 2
        ret = mid * mid
        if ret > x:
            right = mid
        else:
            if x - ret > 0.000001:
                left = mid
            else:
                return mid
    return -1

print(my_sqrt(4))
print(my_sqrt(8))