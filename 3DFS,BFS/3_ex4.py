# 재귀함수 예제2 - 종료 조건 추가

def recursive_func(i):
    if i == 11:
        return
    print(i,"번째 재귀함수에서 ", i+1, "번째 재귀함수를 호출합니다")
    recursive_func(i+1)
    print(i,'번째 재귀함수 종료합니다')

recursive_func(1)