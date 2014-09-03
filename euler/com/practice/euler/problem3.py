'''
Created on Sep 3, 2014

@author: parsa12
'''

import math

def isPrime(i):
    for j in range(2, int(math.sqrt(i)),1):
        if i%j == 0:
            return False
    return True

def primeFactor(num, largestFactor=1):
    
    if num < largestFactor:
        return largestFactor
    
    for i in range(2, int(math.sqrt(num))+1,1):
        if num%i == 0 and isPrime(i):
            # got the factor
            num=num/i
            if largestFactor > i:
                return primeFactor(num,largestFactor)
            else:
                return primeFactor(num,i)
    if largestFactor == 1:
        return 1
    else:
        return num

if __name__ == '__main__':
    print(primeFactor(600851475143))