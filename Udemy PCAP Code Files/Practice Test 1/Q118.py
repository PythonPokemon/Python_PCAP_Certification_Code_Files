
i = 4
while i > 0:    # i is 4
    i -= 2      # i is 2
    print('*')  # *
    if i == 2:  # Yip, i is 2
        break   # Leave the loop directly
else:           # Does not apply, because the break got triggered
    print('*')
