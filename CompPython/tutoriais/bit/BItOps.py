'''
Created on 6 de dez de 2016

@author: C.Lucas
'''

def rmsb(n):
    return n & (-n)

print(rmsb(4))
#print([rmsb(x) for x in range(0, 2 << 12)])

if __name__ == '__main__':
    pass