
def func(number):
    return number      # works and only 7 would be printed
    # print(number)    # works, but 7 & None would be printed
    # print('number')  # works, but number & None would be printed
    # return 'number'  # works, but number would be printed


print(func(7))
