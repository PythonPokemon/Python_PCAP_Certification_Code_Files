
s = lambda x: 0 if x == 0 else 1
s = lambda x: 0 if x == 0 else 1 if x > 0 else -1

print(s(-273.15))  # -1

x = -273.15
res = 0
if x == 0:
    res = 0
elif x > 0:
    res = 1
else:
    res = -1

