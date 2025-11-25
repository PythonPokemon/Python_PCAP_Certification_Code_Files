
num = 2
while num <= 100:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime == True:
        print(num)  # 2 -> 3 -> 5 -> ... -> 89 -> 97
    num += 1

print('----------')

num = 2
is_prime = True
while num <= 100:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime == True:
        print(num)  # 2 -> 3
    num += 1

print('----------')

num = 2
while num <= 100:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime == False:
        print(num)  # 4 -> 6 -> 8 -> ... -> 99 -> 100
    num += 1

print('----------')

stop = 0  # Just added to prevent the infinite loop

num = 2
while num <= 100:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime == True:
        print(num)  # 2 -> 2 -> 2 -> ... -> 2 -> 2

    stop += 1
    # Just added to prevent the infinite loop
    if stop > 100:
        break
    # Just added to prevent the infinite loop
