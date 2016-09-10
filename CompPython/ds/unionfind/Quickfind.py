'''
Created on Jun 3, 2016

@author: christoffer

http://algs4.cs.princeton.edu/15uf/
http://algs4.cs.princeton.edu/15uf/QuickFindUF.java.html

http://marathoncode.blogspot.com.br/search/label/union-find
http://br.spoj.com/problems/REDOTICA/
http://br.spoj.com/problems/TEOBALDO/
http://www.spoj.com/problems/PT07Y/
https://charieblog.wordpress.com/2011/09/15/list-of-interesting-problems-on-spoj/
'''

'''
using urllib2 python 3
https://docs.python.org/3/howto/urllib2.html
'''
from urllib import request

from sys import stdout


def openOnlineFile(url):
    _file = request.urlopen(url)
    for line in _file:
        stdout.write("%s" % (line))

class Quickfind(object):
    '''
    classdocs
    '''
    id = []
    def __init__(self, sz):
        '''
        Constructor
        '''
        self.id     = [x for x in range(0, sz)]
        self.count  = sz
        None
     
    def connected(self, p, q):
        self.validate(p)
        self.validate(q)
        return id[p] == id[q]
     
    def find(self, p):
        self.validate(p)
        return id[p]
    
    '''
    Exception
    https://docs.python.org/3/tutorial/errors.html
    '''
    
    def validate(self, n):
        if(n < 0 or n >= len(self.id)):
            print("indice fora dos limites")
            raise
        
    def union(self, p, q):
        self.validate(p)
        self.validate(q)
        pId = id[p]
        qId = id[q]
        
        # p e q estao no mesmo conjunto
        if(pId == qId):
            return
        
        for i in range(0, len(self.id)):
            if(id[i] == pId):
                id[i] = qId
        self.count -= 1

qf = Quickfind(3)
qf.validate(2)

files = [
    'http://algs4.cs.princeton.edu/15uf/tinyUF.txt'
    ,'http://algs4.cs.princeton.edu/15uf/mediumUF.txt'
    ,'http://algs4.cs.princeton.edu/15uf/largeUF.txt'
]

openOnlineFile(files[0])
    
if __name__ == '__main__':
    pass