import time
start_time = time.process_time()

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

with (open("1003/sample_input.txt", "r")) as f:
  lines = f.readlines()
  
  n = int(lines[0].strip())
  
  for line in lines[1:]:
    result = fibo(int(line.strip()))
    print(f"{result[0]} {result[1]}")


end_time = time.process_time()
print(f"time elapsed : {(end_time - start_time)}ms")