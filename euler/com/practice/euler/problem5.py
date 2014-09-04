'''
Created on Sep 4, 2014

@author: parsa12
'''

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def lcm(a,b):
    return (a*b)/gcd(a,b)

if __name__ == '__main__':
    nums = [x for x in range(2,21,1)]
    
    while(len(nums) > 1):
        num = lcm(nums[0],nums[1])
        nums = nums[2:]
        nums.append(num)
    print(nums[0])