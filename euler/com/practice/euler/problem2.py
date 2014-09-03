'''
https://projecteuler.net/problem=2

Created on Sep 3, 2014

@author: parsa12
'''

def evenFibonacci():
    i=1
    j=2
    sumAll=0
   
    while j < 4000000:
        temp = i 
        i = j
        j = j + temp
       
        if i%2 == 0:
            sumAll=sumAll+i

    return sumAll
        
if __name__ == '__main__':
    print(evenFibonacci())