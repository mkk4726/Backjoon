from sys import stdin as s

s = open('1006/sample_input.txt', 'rt')

# area_cnt : 지역의 개수 / 2
# enemy_copy_dict: 지역별 적의 수를 가지는 dict
# 해당 지역에서 지역을 만족하는 , 제일 적이 많은 지역을 찾는 함수
def find_best(area):
  candidate_list = []
  if (area > area_cnt):
    if (area - 1 == area_cnt): candidate_list.append(area_cnt * 2)
    else: candidate_list.append(area - 1)
    
    if (area == area_cnt * 2 ): candidate_list.append(area_cnt + 1)
    else: candidate_list.append(area + 1)
    
    candidate_list.append(area - area_cnt)
  else:
    if (area - 1 == 0): candidate_list.append(area_cnt)
    else: candidate_list.append(area - 1)
    
    if (area == area_cnt): candidate_list.append(1)
    else: candidate_list.append(area + 1)
    
    candidate_list.append(area + area_cnt)
    
  try:
    return max([(enemy_dict[candidate], candidate) for candidate in candidate_list 
                if enemy_dict[candidate] + enemy_dict[area] <= member_cnt])[1]
  except: # if there is no candidate
    return False  

N = int(s.readline().strip())
  
for _ in range(N):
  # 입력값 받기
  area_cnt, member_cnt = map(int, s.readline().split())
  
  enemy_cnt_list_1 = list(map(int , s.readline().split()))
  enemy_cnt_list_2 = list(map(int , s.readline().split()))
  enemy_cnt_list = enemy_cnt_list_1 + enemy_cnt_list_2
  
  enemy_dict = {} # 지역별 적 수 저장하기 위한 dict
  for i, enemy_cnt in enumerate(enemy_cnt_list):
    enemy_dict[i + 1] = enemy_cnt
  # 문제풀이
  # 순서를 바꿔가면서 찾는다. 1부터시작, 2부터시작, 3부터시작...16부터시작
  result_cnt = 0
  for i in range(1, area_cnt * 2 + 1):
    candidate = find_best(i)
    
