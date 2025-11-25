
print(bool(23))       # True
print(bool(''))       # False
print(bool(' '))      # True
print(bool([False]))  # True

print()

print(bool(''))        # False
print(bool(0))         # False
print(bool(0.0))       # False
print(bool(0j))        # False
print(bool(None))      # False
print(bool([]))        # False
print(bool(()))        # False
print(bool({}))        # False
print(bool(set()))     # False
print(bool(range(0)))  # False
