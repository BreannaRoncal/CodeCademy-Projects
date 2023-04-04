def iterative_fibonacci(num):
  fibs = [0, 1]
  if num < 0:
    return -1
  if num <= 1:
    return fibs[num]
  while num > len(fibs) - 1:
    fibs.append(fibs[-2] + fibs[-1])
  return fibs[-1]


# test cases
print(fibonacci(3) == 2)
print(fibonacci(7) == 13)
print(fibonacci(0) == 0)
print(fibonacci(-1) == -1)
