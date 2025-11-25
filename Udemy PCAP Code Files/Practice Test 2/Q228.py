
x = """
"""
print(len(x))  # 1

# ord() returns an integer representing the Unicode character.
print(ord(x[0]))  # 10 (LF: line feed, new line)

# Same result with single quotes:
y = '''
'''
print(len(y))  # 1

# Every line feed is a character:
z = """

"""
print(len(z))  # 2
