import heapq
from sys import stdin, setrecursionlimit
setrecursionlimit(10**6) # 파이썬 최대 재귀깊이 높이기

stdin = open('1655/sample_input.txt', 'rt') # 테스트할 때, 제출할 때는 주석처리 해주기

n = int(stdin.readline().strip())

# python에서 제공하는 heap은 min heap. root node에 가장 작은 값이 옴.
# 따라서 max heap을 사용하기 위해 입력값을 음수로 바꿔 입력
left_heap = [] # max heap
right_heap = [] # min heap

for _ in range(n):
  input_number = int(stdin.readline().strip())
  
  # left heap의 개수가 right heap의 개수보다 항상 많거나 같아야 left heap의 root node가 median을 가짐 
  # left heap과 right heap의 개수 맞춰주기
  if (len(left_heap) == len(right_heap)):
    heapq.heappush(left_heap, -input_number)
  else:
    heapq.heappush(right_heap, input_number)
  
  # left_heap(max heap)이 right_heap(min heap)보다 클 때 -> 두 개의 위치를 바꿔준다. 
  if right_heap and -left_heap[0] > right_heap[0]:
    left_number = heapq.heappop(left_heap)
    right_number = heapq.heappop(right_heap)
    
    heapq.heappush(left_heap, -right_number)
    heapq.heappush(right_heap, -left_number)
    
  # left heap (max heap)에서 정답 꺼내기
  print(-left_heap[0])
    
    