'''
N = 1260 (N은 10의 배수)
거스름돈 종류: 500, 100, 50, 10
>> 거슬러줘야할 동전의 최소 개수
'''

N = 1260
count = 0
coin_arr = [500, 100, 50, 10]

for coin in coin_arr:
    count = count + (N//coin)
    N = N % coin

print(count)