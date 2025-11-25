
nums = [3, 7, 23, 42]
alphas = ['p', 'p', 'm', 'j']

print(nums is alphas)  # False
print(nums == alphas)  # False

print(id(nums))    # e.g. 140539383947452
print(id(alphas))  # e.g. 140539383900864 (a different number)

nums = alphas

print(nums is alphas)  # True
print(nums == alphas)  # True

print(nums)    # ['p', 'p', 'm', 'j']
print(alphas)  # ['p', 'p', 'm', 'j']

print(id(nums))    # e.g. 140539652049216
print(id(alphas))  # e.g. 140539652049216 (the same number)
