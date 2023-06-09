import time
start_time = time.process_time()

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

with (open("1005/sample_input.txt", "r")) as f:
  lines = f.readlines()

  N = int(lines[0].strip())
  
  tmp_cnt = 1 # vscode에서 입력값 받기 위한 값
  
  for _ in range(N):
    # 입력값 받기
    node_cnt, way_cnt = map(int, lines[tmp_cnt].strip().split())
    tmp_cnt += 1 # 무시하기
    cost_list = list(map(int , lines[tmp_cnt].strip().split()))
    tmp_cnt += 1 # 무시하기
    
    ways_dict = {} # 완료까지 필요한 노드경로 넣기
    cost_dict = {} # 노드마다 필요한 cost 저장해놓기
    
    for i in range(way_cnt):
      start_node, end_node = map(int, lines[tmp_cnt+i].strip().split())
      if (end_node in ways_dict.keys()): ways_dict[end_node].append(start_node)
      else: ways_dict[end_node] = [start_node]
    tmp_cnt += way_cnt # 무시하기 
    final_node = int(lines[tmp_cnt].strip())
    tmp_cnt += 1 # 무시하기
    print(checkCost(final_node))
    # 문제풀이
    
    
    


end_time = time.process_time()
print(f"time elapsed : {(end_time - start_time)}ms")