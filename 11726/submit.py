from sys import stdin, setrecursionlimit
setrecursionlimit(10**6) # 파이썬 최대 재귀깊이 높이기

stdin = open('11726/sample_input.txt', 'rt') # 테스트할 때, 제출할 때는 주석처리 해주기

cnt_dict = {}
cnt_dict[1] = 1; cnt_dict[2] = 2

def find_cnt(n: int) -> int:
  """
  n: 가로넓이
  """
  if (n in cnt_dict.keys()): return cnt_dict[n]
  
  cnt_dict[n] = find_cnt(n - 1) + find_cnt(n - 2)
  return cnt_dict[n]

N = int(stdin.readline().strip())
cnt = find_cnt(N)
print(cnt % 10007)
