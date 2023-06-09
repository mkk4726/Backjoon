def check_InOrOut(point: tuple, planet:tuple):
  x, y = point
  a, b, r = planet
  d = ((x - a) ** 2 + (y - b)**2) ** 0.5
  if (d > r):
    return False
  else:
    return True


N = int(input())

for _ in range(N):
  x1, y1, x2, y2 = map(int, input().split())
  n = int(input())
  total_cnt = 0
  for _ in range(n):
    a1, a2, r1 = map(int, input().split())
    result1 = check_InOrOut((x1, y1), (a1, a2, r1)) # 출발점이 planet 안에 있는지
    result2 = check_InOrOut((x2, y2), (a1, a2, r1)) # 도착점이 planet 안에 있는지
    if (result1 != result2): total_cnt += 1 # 둘 중에 하나만 들어있으면 +1 해주기

  print(total_cnt)
