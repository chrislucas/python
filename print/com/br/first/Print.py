'''
Created on Dec 21, 2015
http://www.vogella.com/tutorials/Python/article.html
http://www.vexorian.com/
@author: christoffer
'''
def add(a, b):
    return a + b

def euclides(a, b):
    if a%b == 0 :
        return b
    else :
        return euclides(b, a%b)

print euclides(58, 4)
