'''
Created on 30 de nov de 2016

@author: C.Lucas
'''

#!/bin/python3

# https://www.hackerrank.com/contests/w26/challenges/game-with-cells/leaderboard

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]

m = m // 2 + m % 2
n = n // 2 + n % 2

print(m*n)

if __name__ == '__main__':
    pass