from sys import stdin

stdin = open('1006/sample_input.txt', 'rt')

N = int(stdin.readline().strip())
  
for _ in range(N):
  # 입력값 받기
  area_cnt, member_cnt = map(int, stdin.readline().split())
  
  enemy_cnt_list_1 = list(map(int , stdin.readline().split()))
  enemy_cnt_list_2 = list(map(int , stdin.readline().split()))
  enemy_cnt_list = enemy_cnt_list_1 + enemy_cnt_list_2
  
  enemy_dict = {} # 지역별 적 수 저장하기 위한 dict
  for i, enemy_cnt in enumerate(enemy_cnt_list):
    enemy_dict[i + 1] = enemy_cnt
  
  # 문제풀이
  