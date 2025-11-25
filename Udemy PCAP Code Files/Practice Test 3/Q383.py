
pairs = [[2, 1], [-1, -1]]
new_pairs = map(lambda p: sorted(p), pairs)
print(list(new_pairs))        # [[1, 2], [-1, -1]]
new_pairs = map(lambda p: sorted(p), pairs)
print(list(new_pairs)[0][0])  # 1
