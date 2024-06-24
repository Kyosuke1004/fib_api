# 与えられたn番目のフィボナッチ数を計算して返す
def calculation_fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# 正の整数が代入されているか判定
def check_positive_int(value):
    try:
        num = int(value)
        if num > 0:
            return True
        else:
            return False
    except ValueError:
        return False