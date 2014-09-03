'''
https://projecteuler.net/problem=1

Created on Sep 2, 2014
@author: parsa12
'''


def multiple3or5():
    sumAll=0
    for i in range (3,1000,1):
        if i % 3 == 0 and i % 5 == 0:
            sumAll=sumAll+i
        elif i % 5 == 0:
            sumAll=sumAll+i
        elif i % 3 == 0:
            sumAll=sumAll+i
    return sumAll
        
if __name__ == '__main__':
    print(multiple3or5())