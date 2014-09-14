import math as m

def isPrime(n):  
    if n <= 1:  
        return False
    else:
        for i in range (2, int (m.sqrt (n)) + 1):
           if n % i == 0:
              return False
        return True

n = int (m.sqrt (600851475143)) + 1
print n
print isPrime (n)
while ( isPrime (n) == False or 600851475143 % n != 0):
   n -= 1
print n
