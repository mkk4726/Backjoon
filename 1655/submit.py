from sys import stdin, setrecursionlimit
setrecursionlimit(10**6) # 파이썬 최대 재귀깊이 높이기

stdin = open('1655/sample_input.txt', 'rt') # 테스트할 때, 제출할 때는 주석처리 해주기


def get_median(n_l: list) -> int:
  length = len(n_l)
  
  if (length == 1): return n_l[0]
  
  if (length % 2 == 0): return min(n_l[length // 2 - 1], n_l[length // 2]) 
  else: return n_l[length // 2]  

n = int(stdin.readline().strip())

number_list = []
for _ in range(n):
  number = int(stdin.readline().strip())

  if len(number_list) == 0: 
    number_list.append(number)
    print(number)
    continue
  
  start = 0; end = len(number_list) - 1
  while (start < end):
    middle = (start + end) // 2
    if (number == number_list[middle]): break
    if (number < number_list[middle]): end = max(0, middle - 1)
    else: start = min(len(number_list)-1, middle + 1)
    
  middle = (start + end) // 2
  if (number <= number_list[middle]): number_list.insert(middle, number)
  else: number_list.insert(middle + 1, number)
                  
  print(get_median(number_list))   
  
    
    
    

  
  
  
