'''
Created on 9 de ago de 2016

@author: C.Lucas
'''

'''
https://www.hackerrank.com/challenges/even-odd-query
'''

def fastexp(b, e):
    if(e == 0):
        return 1

def find(_list, x, y):
    if(x > y):
        return 1
    e = find(_list, x+1, y)
    ans = fastexp(_list[x], e)
    return ans

if __name__ == '__main__':
    pass