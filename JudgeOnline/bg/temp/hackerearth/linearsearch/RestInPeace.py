'''
Created on Jun 9, 2016

@author: christoffer
https://www.hackerearth.com/problem/algorithm/rest-in-peace-21-1/
DONE
'''
from sys import stdin, stdout
'''
Funcao que procura um numero dentro de outro
exemplo
Procurar se tem
'''
def hasSubNumber(m, n):
    m = str(m)
    n = str(n)
    return n in m

def run():
    cases = int(stdin.readline())
    while cases > 0:
        number  = int(stdin.readline())
        msg     = 'The streak is broken!' if ((number % 21) == 0 or hasSubNumber(number, 21)) else 'The streak lives still in our heart!'
        stdout.write("%s\n" % (msg))
        cases -= 1
run()

if __name__ == '__main__':
    pass