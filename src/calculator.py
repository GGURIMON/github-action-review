# 더히기 Test
def add(a, b):
    return a + b

# 빼기
def subtract(a, b):
    return a - b

# 곱하기
def multiply(a, b):
    return a * b

# 나누기
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("0으로 나눌 수 없습니다.")
    return a / b
