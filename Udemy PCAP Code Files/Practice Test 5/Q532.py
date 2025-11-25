
str1 = 'Peter'
str2 = str1[:]
# str2 = str1        # The same thing

print(id(str1))  # e.g. 140539652049216
print(id(str2))  # e.g. 140539652049216 (the same number than str1)
print(str1 is str2)  # True
print(str1 == str2)  # True
