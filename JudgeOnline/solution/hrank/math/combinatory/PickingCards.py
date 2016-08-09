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
        n = 0
        picked = 0
        combination = 1
        while True:
            if n in freq:
                picked += freq[n]
            
            if picked > 0:
                combination = ((combination % MOD) * (picked % MOD)) % MOD
                picked -= 1
                n += 1
            else:
                break
    return freq

frequency([0,0,1,2])


if __name__ == '__main__':
    pass