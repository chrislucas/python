'''
Created on 24 de nov de 2016

@author: christoffer
'''

# http://br.spoj.com/problems/POLEPOS/


from sys import stdin as _in, stdout as _out


def readIntList(fmt):
    return [int(e) for e in _in.readline().split(fmt)]
    
def run():
    while(True):
        num = int(_in.readline().strip("\n"))
        pos = [0] * num
        acc = 0
        if(num == 0):
            break
        f = True
        for idx in range(0, num):            
            c, p = [int(x) for x in _in.readline().rstrip('\n').split(" ")]
            if(pos[idx + p] != 0):
                f = False
            pos[idx + p] = c
    
        if(f):
            print(*pos)
        else:
            print(-1)
    
run()


if __name__ == '__main__':
    pass