
print(len([i for i in range(0, -2)]))      # 0

# Those make more sense:
print(len([i for i in range(-2, 0)]))      # 2
print(len([i for i in range(0, -2, -1)]))  # 2
