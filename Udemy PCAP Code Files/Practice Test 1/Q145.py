
x = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]


def func(data):
    print('data:', data)    # [[1, 2], [3, 4]]
    res = data[0][0]        # 1
    print('res:', res)
    for da in data:
        print('da:', da)    # [1, 2] -> [3, 4]
        for d in da:
            print('d:', d)  # 1 -> 2 -> 3 -> 4
            if res < d:
                res = d
    return res


print(func(x[0]))              # 4

print(func([[1, 7], [3, 4]]))  # 7
