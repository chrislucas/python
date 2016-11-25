'''
Created on 25 de nov de 2016

@author: C.Lucas
'''

# http://br.spoj.com/problems/CPCARROS/

class Pa():
    def __init__(self, prefix, suffix):
        self.prefix = prefix
        self.suffix = suffix
        return None
    
    def gt(self):
        return 'v'

class Pn():
    def __init__(self, prefix, suffix):
        self.prefix = prefix
        self.suffix = suffix
        return None
    
    def gt(self):
        return 'n'
    

if __name__ == '__main__':
    pass