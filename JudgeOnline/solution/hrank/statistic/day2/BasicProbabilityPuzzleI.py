'''
Created on 30 de mar de 2016

@author: C.Lucas
'''
'''
Probabilidade condicional
'''

# https://www.hackerrank.com/contests/intro-to-statistics/challenges/basic-probability-puzzles-1
# (3,6) (2,7) (1,8)

#print( "%f" % (3 / 12) )

#https://brilliant.org/wiki/cryptogram-problem-solving/

#https://brilliant.org/wiki/probability-problem-solving/
#https://brilliant.org/wiki/rsa-encryption/?utm_campaign=wiki-writers&utm_medium=bnotif&utm_source=brilliant&utm_content=wiki-rsa-encryption&from_notification=7963585

#https://brilliant.org/wiki/factorials-properties/#factorials-problem-solving-basic
#https://brilliant.org/problems/last-2/
def fat(n):
    i = n
    while n > 2:
        n = n - 1
        i = (i * n) % 100
    return i

def test():
    s = 0
    for i in range(5, 100, 5):
        s = (s + fat(i) ) % 100 
    return s

print(test() + 1) 

if __name__ == '__main__':
    pass