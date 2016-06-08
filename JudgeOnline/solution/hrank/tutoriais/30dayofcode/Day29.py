'''
Created on Jun 8, 2016

@author: christoffer
https://www.hackerrank.com/challenges/30-bitwise-and?h_r=email&h_v=30_days_of_code_backfill_full&unlock_token=30602972a3da037ad5ef9cda891de74734ccc65e&utm_campaign=30_days_of_code_continuous&utm_medium=email&utm_source=daily_reminder
'''
'''
Estudar depois
https://en.wikipedia.org/wiki/Bitwise_operation#AND
http://www.geeksforgeeks.org/find-maximum-subset-xor-given-set/
http://www.geeksforgeeks.org/find-the-maximum-subarray-xor-in-a-given-array/
'''


from sys import stdin, stdout


def maxSubsetXOR(n):
    return None


'''
Naive Approach
'''
def maxOpAndO2(n, k):
    max = 0
    for i in range(1, n):
        for j in range(i+1, n+1):
            opAnd = i & j
            if( opAnd > max and opAnd < k):
                max = opAnd
    return max

def maxOpAndV2(n, k):
    max = 0
    return max


'''
Pesquisar como achar o bit menos significativo
'''

def leastSigniticantBitON(n):
    idx = 0
    while (n & 1) > 0:
        n >>= 1
        idx += 1
    return idx

def leastSigniticantBitO1(n):
    return n & (-n)

def maxOpAndBitSol(n, k):
    a = k-1
    b = (~a) & -(~a)
    if(a | b) > n:
        return (a - 1)
    return a

def solution():
    cases = int(stdin.readline())
    for i in range(0, cases):
        n, k = stdin.readline().split(" ")
        n, k = [int(n), int(k)]
        stdout.write("%d\n" % (maxOpAndBitSol(n, k)))

solution()
#print(maxOpAndBitSol(17, 16))
#print("%d %d" % (leastSigniticantBitO1(10), leastSigniticantBitON(10)))
#https://www.hackerrank.com/challenges/30-bitwise-and/editorial
if __name__ == '__main__':
    pass