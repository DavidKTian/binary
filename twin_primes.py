def is_prime(x):
  factors = []
  for i in range(1,x+1):
    if x%i == 0:
      factors.append(i)
  if len(factors) == 2:
    return True
  else:
    return False
def twins(a,b):
  if is_prime(a) == True and is_prime(b) == True:
    if abs(b-a) != 2:
      print(a, "and", b, "are primes but not twin primes")
    elif abs(b-a) == 2:
      print(a,"and", b, "are twin primes.")
  else: 
    print(a, "and",b,"are not twin primes")
