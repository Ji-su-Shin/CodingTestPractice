# 그리디

현재 상황에서 지금 당장 좋은 것만 고르는 방법
미래에 미칠 영향에 대해선 고민하지 않음

## 예제 1 거스름돈

1. 해결 아이디어: 가장 큰 화폐 단위부터 거슬러준다.
2. 그리디 알고리즘의 정당성
   - 가지고 있는 동전 중 단위가 큰 동전은 단위가 작은 동전의 "배수"이기 때문.
   - 즉, 만약 큰 단위 동전이 작은 단위 동전의 배수가 아니라면 그리디로 풀 수 없음.
   - 대부분의 그리디 알고리즘 문제에서는 이처럼 누제 풀이를 위한 최소한의 아이디어를 떠올리고 이것이 정당한지 검토할 수 이어야 답을 도출할 수 있다.ㅇ

## 실전문제 1 큰 수의 법칙

해결 아이디어: 가장 큰 수와 두 번째로 큰 수만 가지고 규칙에 맞춰 더하면 된다.
유사 문제에 대한 아이디어: "반복되는" 수열에 대해 파악해야 한다. 반복되는 수를 파악해서 반복문이 아니라 바로 더해주어야 함.

1. 입력 조건
   - 첫째 줄에,
        N(2 <= N <= 1000)
        M(1 <= M <= 10000)
        K(1 <= K <= 10000)
    의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
   - 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10000 이하의 수로 주어진다.
   - 입력으로 주어지는 K는 항상 M보다 작거나 같다.
2. 출력 조건
   - 첫째 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다.
3. 입력 예시
   5 8 3
   2 4 5 4 6
4. 출력 예시
   46

## 실전문제 2 숫자 카드 게임

## 실전문제 3 1이 될 때까지