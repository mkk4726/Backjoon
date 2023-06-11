test = [(1, 2), (2, 3), (3, 4)]
print(max(test))
# print(max([]))
if([1,2]):
  print('ok')

tmp = {1: (1, 2), 2: (2, 3), 3: (4, 5), 4: (5, 6)}
print([value for value in tmp.items()])
tmp[1] = (1, 3)
print(tmp[1][1])