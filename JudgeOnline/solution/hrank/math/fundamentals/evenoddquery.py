'''
Created on 9 de ago de 2016

@author: C.Lucas
'''

'''
https://www.hackerrank.com/challenges/even-odd-query
DONE BARALHO
'''

from sys import stdin

def fastexp(b, e, mod=int(1E9)+7):
    if(e == 0):
        return 1
    elif(e == 1):
        return b
    '''
    elif(e < 0):
        e = -e
        b = 1/b
    '''
    ans = 1
    while(e>=1):
        if( (e & 1) == 1):
            ans = ((ans%mod) * (b%mod)) % mod
        e >>= 1
        b = ((b%mod) * (b%mod)) % mod
    return ans
'''
def find(nums, x, y):
    if(x > y):
        return 1
    e = find(nums, x+1, y)
    a = fastexp(nums[x], e)
    return a

def fx(nums, x, y):
    if(x > y):
        return 1
    a = fastexp(nums[y], 1)
    y -= 1
    while(y >= x):
        a = fastexp(nums[y], a)
        y -= 1
    return a
'''

# funciona mais da TLE
def fn(nums, x, y):
    expo = nums[y]
    y -= 1
    while(y >= x):
        expo = nums[y] if expo != 0 else 1
        y -= 1
    return expo

def fx(nums, x, y):
    if(x == y):
        # return 1 if nums[x] == 0 else nums[x] & 1
        return nums[x] & 1
    else:
        return nums[x] & 1 if nums[x+1] != 0 else 1
    
def read(fmt = ""):
    enter = stdin.readline().strip("\n")
    return enter if(fmt == "") else enter.split(fmt)

def readInt(fmt = ""):
    return int(read(fmt))

def readInts(fmt = " "):
    return [int(x) for x in read(fmt)]

def run():
    N = readInt()
    nums = readInts()
    Q = readInt()
    #F = open("out5.txt", mode='a')
    while(Q > 0):
        x, y = readInts()
        ans = fx(nums, x-1, y-1)
        # http://ss64.com/nt/fc.html
        #print("Odd" if (ans & 1) == 1 else 'Even', file=F)
        print("Odd" if (ans & 1) == 1 else 'Even')
        Q -= 1
run()
#print(fastexp(15, -2))

if __name__ == '__main__':
    pass