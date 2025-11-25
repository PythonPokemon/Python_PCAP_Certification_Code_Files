
with open('data.txt', 'w') as f:
    f.write("I'm gonna make him an offer he can't refuse.")

with open('data.txt', 'r') as f:
    data = f.readlines()
    print(data)  # ["I'm gonna make him an offer he can't refuse."]
    for line in data:
        words = line.split()
        print(words)
