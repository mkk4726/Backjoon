from sys import stdin, setrecursionlimit
setrecursionlimit(10**6) # 파이썬 최대 재귀깊이 높이기

stdin = open('12865/sample_input.txt', 'rt') # 테스트할 때, 제출할 때는 주석처리 해주기

n, k = map(int, stdin.readline().split())

things = []
for _ in range(n):
  w, v = map(int, stdin.readline().split())
  things.append((w, v))

# 계산하기 편하게 0~k까지 만들어서, index 1~k까지로 구현하기
value_list = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
  for j in range(1, k+1):
    # 현재 물건의 가치와 무게
    value = things[i-1][1]; weight = things[i-1][0]
    
    # 아직 담을 수 없다면, 그 전 row에 있는 값 그대로 
    if (j < weight):
      value_list[i][j] = value_list[i-1][j]
    # value_list[i-1] 행은 그 전까지 구해놓은 최적의 값들을 의미
    else: 
      value_list[i][j] = max(value + value_list[i-1][j-weight], value_list[i-1][j])

print(value_list[n][k])
