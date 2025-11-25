
x = 42
y = 7
data = "I'm gonna make him an offer he can't refuse."

print(data.find('an') if data else None)   # 19
print(19 if None else x / y)               # 6.0
print(data.rfind('an') if data else None)  # 32
print(7 if len(data) > 19 else 6)          # 7
