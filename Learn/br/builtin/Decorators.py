'''
Created on 24 de jul de 2016

@author: C.Lucas

http://thecodeship.com/patterns/guide-to-python-function-decorators/
'''

'''
function are first class citizen
'''
def fx():
    return 0x0F1233AA

def passFunction(func):
    return func() & 0xDD
var = fx

def returnFunction():
    def w():
        print(10)
    
    return w

print(passFunction(var))

if __name__ == '__main__':
    pass