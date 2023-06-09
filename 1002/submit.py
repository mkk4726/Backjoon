N = int(input())

for _ in range(N):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    
    if (x1==x2 and y1==y2 and r1==r2): print(-1)
    elif (d == r1 + r2 or d == max(r1,r2) - min(r1, r2)): print(1)
    elif (d < r1 + r2 and max(r1, r2) < d + min(r1, r2)): print(2)
    else: print(0)