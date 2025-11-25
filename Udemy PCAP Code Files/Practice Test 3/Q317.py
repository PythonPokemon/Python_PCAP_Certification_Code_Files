
data = ['Peter', 'Paul', 'Mary', 'Jane']
print('\n'.join(data))

"""
Peter
Paul
Mary
Jane
"""

# print(data.join('\n'))           # AttributeError: ...
# print(data.concatenate('\n'))    # AttributeError: ...
# print(data.join('%s\n', names))  # AttributeError: ...
