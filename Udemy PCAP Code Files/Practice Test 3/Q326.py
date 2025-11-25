
data = {'x': 1, 'y': 2, 'z': 3}
print(data['x', 'y'])      # KeyError: ('x', 'y')

print(data['x'], data['y'])  # 1 2

data = {('x', 'y'): 1}
print(data['x', 'y'])        # 1
