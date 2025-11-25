
try:
    f = open('non_existing_file', 'r')
    print(1, end=' ')
except IOError as error:
    print(error.errno, end=' ')  # 2
    print(2, end=' ')            # 2
else:
    f.close()
    print(3, end=' ')
