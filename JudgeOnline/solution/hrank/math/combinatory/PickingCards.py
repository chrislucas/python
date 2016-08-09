'''
Created on May 31, 2016

@author: christoffer

https://www.hackerrank.com/challenges/picking-cards
https://en.wikipedia.org/wiki/Rule_of_product
'''

MOD = 1000000007;

def fact(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans

def frequency(array):
    freq = {}
    for i in array:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    if len(freq) == 1 :
        return fact(len(array))
    else:
        for k in freq:
            k
        
    return freq

frequency([0,0,1,2])


if __name__ == '__main__':
    pass