
def safe_root(a, b):
    if a >= 0:
        answer = a ** (1 / b)
    elif a % 2 == 0:
        answer = 'Result is an imaginary number'
    else:
        answer = -(-a) ** (1 / b)
    return answer


print(safe_root(9, 2))    # 3.0
print(safe_root(-9, 2))   # -3.0
print(safe_root(-16, 2))  # Result is an imaginary number
