'''
Created on 23 de jun de 2016

@author: chrislucas
DONE
https://www.urionlinejudge.com.br/judge/pt/problems/view/2041
'''
from sys import stdin, stdout

def solve(k):
    strA = '3'
    i = 1
    while i < k:
        counter = 1
        strB = ''
        j = 0
        while j < len(strA)-1:
            if strA[j] == strA[j+1]:
                counter += 1
            else:
                strB = "{0}{1}{2}".format(strB, counter, strA[j])
                counter = 1
            j+=1
        strB = "{0}{1}{2}".format(strB, counter, strA[j])
        strA = strB
        i+=1
    return strA


def init():
    _list = [solve(x) for x in range(1, 41)]
    return _list
    
def run():
    _list = init()
    while True:
        try:
            k = int(stdin.readline())
            stdout.write("%s\n" % (_list[k-1]))
        except:
            break
        
run()

if __name__ == '__main__':
    pass