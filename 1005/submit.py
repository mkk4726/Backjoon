import sys
sys.setrecursionlimit(10**6) # 파이썬 최대 재귀깊이 높이기

# ways_dict : 완료하기위해 해야하는 선행노드 dict
# cost_dict : 시간을 단축하기 위한 node별 cost 저장 dict
def checkCost(node:int) -> int:
  if (node not in ways_dict.keys()): # 최하위 노드
    return cost_list[node - 1]
  if (node in cost_dict.keys()):
    return cost_dict[node]
  
  result = max([checkCost(before_node) for before_node in ways_dict[node]]) + cost_list[node - 1]
  cost_dict[node] = result
  return result

N = int(sys.stdin.readline())
  
for _ in range(N):
  # 입력값 받기
  node_cnt, way_cnt = map(int, sys.stdin.readline().split())
  cost_list = list(map(int , sys.stdin.readline().split()))
  
  ways_dict = {} # 완료까지 필요한 선행노드경로 넣기
  cost_dict = {} # 노드마다 필요한 cost 저장해놓기
  
  for _ in range(way_cnt):
    start_node, end_node = map(int, sys.stdin.readline().split())
    if (end_node in ways_dict.keys()): ways_dict[end_node].append(start_node)
    else: ways_dict[end_node] = [start_node]
  
  final_node = int(input())
  
  # 문제풀이
  print(checkCost(final_node))
  