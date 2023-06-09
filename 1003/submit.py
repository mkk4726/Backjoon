memo_dict = {}
memo_dict[0] = (1, 0)
memo_dict[1] = (0, 1)

def fibo(n: int):
  if (n in memo_dict.keys()):
    return memo_dict[n]
  else:
    result = (fibo(n-1)[0] + fibo(n-2)[0] , fibo(n-1)[1] + fibo(n-2)[1])
    memo_dict[n] = result 
    return result

  
n = int(input())
  
for i in range(n):
  result = fibo(int(input()))
  print(f"{result[0]} {result[1]}")
