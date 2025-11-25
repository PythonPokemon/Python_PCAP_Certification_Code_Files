
strng = "John,Doe,42"
print(strng.split(","))  # ['John', 'Doe', '42']
strng = "".join(strng.split(","))
print(strng)      # JohnDoe42
print(strng[-2])  # "4"
