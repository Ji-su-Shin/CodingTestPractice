# 팩토리얼 예제

## 반복문 사용
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

## 재귀함수 사용
def factorial_recursive(n):
    result = 1
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

print('반복문 사용: ', factorial_iterative(5))
print('재귀문 사용: ', factorial_recursive(5))


