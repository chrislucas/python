'''
Created on May 20, 2016

@author: christoffer
'''


def solIterative(p, j):
    s = 1
    for i in (1, p+1):
        s = (i+j-1)%p+1
    return s

def solRecursive(p, j):
    if(p == 1):
        return p
    else:
        return (solRecursive(p-1, j) + (j-1)) % p + 1
    


print(solIterative(5, 3))
print(solIterative(5, 3))

if __name__ == '__main__':
    pass