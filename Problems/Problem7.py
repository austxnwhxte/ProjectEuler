# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#                           What is the 10001st prime number?


def is_prime(n): #boolean function to test if n is prime
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  # since all primes > 3 are of the form 6n ± 1
  # start with f=5 (which is prime)
  # and test f, f+2 for being prime
  # then loop by 6.
  f = 5
  while f <= r:
    #print('\t',f)
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True

count = 0
numtotest = 0
while count < 10001:
    numtotest +=1
    if is_prime(numtotest) == True:
        count += 1
        print("prime index", "|", "prime")
        print(count, "       |", numtotest)

print("the 10001st prime is:", numtotest)
