import gc
gc.disable()
def test(upper_bound):
    result = 0.0
    for i in range(0, upper_bound):
        result += i ** 2
        result = result / 100000.0
    return result