'''
Created on Sep 3, 2014

@author: parsa12
'''

import problem3

def isPalindrome(i):
    mid = int(len(str(i))/2)
    palindrome = str(i)
    
    for count in range(0,mid):
        if (palindrome[count] != palindrome[len(palindrome)-1-count]):
            return False
    return True

def reduce(factors, maxVal, reducedSize):
    if reducedSize <= 0 or len(factors) < reducedSize:
        return False
    
    if len(factors) == reducedSize:
        print(factors)
        return True

    
    if factors[0]*factors[-1] <= maxVal:
        factorsNew = [factors[0]*factors[-1]]
        factorsNew.extend(factors[1:-1])
        return reduce(factorsNew,maxVal,reducedSize)
    else:
        return reduce(factors[1:],maxVal,reducedSize-1)
    

def largestPalidromeProduct():
    for i in range(997002, 100000, -1):
        if isPalindrome(i):
            if (problem3.primeFactor(i) > 999):
                continue
            else:
                primefactor=problem3.primeFactor(i)
                factors=[]
                j=i
                while primefactor != 1:
                    factors.append(primefactor)
                    j = j/primefactor
                    primefactor = problem3.primeFactor(j)
                # sort the factors
                factors = sorted(factors,reverse=True) 
                success = reduce(factors,999,2)
                if success:
                    print(i)
                    break
                else:
                    continue
    
if __name__ == '__main__':
    print(largestPalidromeProduct())
    
    
    
    