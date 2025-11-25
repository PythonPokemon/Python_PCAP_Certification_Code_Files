
s = 'rhyme'
s = s[::2]
print(s)  # rye

s = 'rhyme'
s = s[::-2]
print(s)  # eyr

s = 'rhyme'
# s = s[9]  # IndexError: string index out of range

s = 'rhyme'
s[0] = s[1]
# TypeError: 'str' object does not support item assignment
