import time
start_time = time.process_time()

def check_InOrOut(point: tuple, planet:tuple):
  x, y = point
  a, b, r = planet
  d = ((x - a) ** 2 + (y - b)**2) ** 0.5
  if (d > r):
    return False
  else:
    return True


with (open("1004/sample_input.txt", "r")) as f:
  lines = f.readlines()

  N = int(lines[0].strip())
  
  tmp_cnt = 1 # vscode에서 입력값 받기 위한 값
  
  for _ in range(N):
    x1, y1, x2, y2 = map(int, lines[tmp_cnt].strip().split())
    tmp_cnt += 1 # 무시하기
    n = int(lines[tmp_cnt].strip())
    tmp_cnt += 1 # 무시하기
    
    total_cnt = 0 # 진입/이탈 여부 횟수

    for i in range(n):
      a1, a2, r1 = map(int, lines[tmp_cnt+i].strip().split())
      result1 = check_InOrOut((x1, y1), (a1, a2, r1)) # 출발점이 planet 안에 있는지
      result2 = check_InOrOut((x2, y2), (a1, a2, r1)) # 도착점이 planet 안에 있는지
      if (result1 != result2): total_cnt += 1 # 둘 중에 하나만 들어있으면 +1 해주기

    tmp_cnt += n # 무시하기 
    print(total_cnt)
    


end_time = time.process_time()
print(f"time elapsed : {(end_time - start_time)}ms")