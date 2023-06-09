# import os

# print(os.listdir())

# 현재 파일위치말고 terminal 위치에서 상대경로가 결정됨 
# 백준에서 읽을 때와는 다름
with (open("1002/sample_input.txt", "r")) as f:
  lines = f.readlines()
  
  N = int(lines[0].strip())
  
  for line in lines[1:]:
    input = line.strip()
    x1, y1, r1, x2, y2, r2 = map(int, input.split())
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 # 거리 구하기
    
    if (x1==x2 and y1==y2 and r1==r2): print(-1) # 완전히 같을 때
    elif (d == r1 + r2 or d == max(r1,r2) - min(r1, r2)): print(1) # 내접, 외접
    elif (d < r1 + r2 and max(r1, r2) < d + min(r1, r2)): print(2) # 겹칠 때
    else: print(0) # 그 외의 경우 

    


f.close()