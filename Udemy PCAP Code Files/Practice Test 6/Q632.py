
data = [10, 2, 1, 7, 5, 6, 4, 3, 9, 8]

def find_high_low(nums):
    nums.sort()
    print(nums)                        
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return nums[-1], nums[0]
    # return nums[len(nums)], nums[0]
    # IndexError: list index out of range
    # return nums[0], nums[-1]
    # high and low are interchanged

high, low = find_high_low(data)

print(
    ('The highest number is {} ' +
     'and the lowest number is {}.').format(high, low)
)
# The highest number is 10 and the lowest number is 1.
