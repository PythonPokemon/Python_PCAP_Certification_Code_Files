
class A:
    __value = 1


print(A._A__value)  # 1
# print(A.__value)
# AttributeError: type object 'C' has no attribute '__value'


import sys
print(sys.path)
# ['/Users/cordm/.../Practice Test 5',
# '/Users/cordm/...',
# '/Library/Frameworks/Python.framework/Versions/3.9/lib/python39.zip',
# '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9',
# '/Library/Frameworks/.../Versions/3.9/lib/python3.9/lib-dynload',
# '/Users/cordm/Library/Python/3.9/lib/python/site-packages',
# '/Library/Frameworks/.../Versions/3.9/lib/python3.9/site-packages']
