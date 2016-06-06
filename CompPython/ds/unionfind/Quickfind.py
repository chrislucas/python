'''
Created on Jun 3, 2016

@author: christoffer

http://algs4.cs.princeton.edu/15uf/
http://algs4.cs.princeton.edu/15uf/QuickFindUF.java.html
'''

class Quickfind(object):
    '''
    classdocs
    '''
    id = []
    def __init__(self, n):
        '''
        Constructor
        '''
        self.id = [x for x in range(0, n)]
        None
     
    def connected(self, p, q):
        return id[p] == id[q]
     
    def find(self, p):
        return id[p]
    
    def union(self, p, q):
        pId = id[p]
        qId = id[q]
        
        if(pId == qId):
            return
        
        for i in range(0, len(self.id)):
            if(id[i] == pId):
                id[i] = qId

qf = Quickfind(2)
    
if __name__ == '__main__':
    pass