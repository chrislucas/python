'''
Created on 10 de out de 2016

@author: C.Lucas

http://www.bogotobogo.com/python/python_PriorityQueue_heapq_Data_Structure.php
'''

from queue import PriorityQueue

def run_test_1():
    pq = PriorityQueue()
    pq.put( (12, 'doze'))
    pq.put( (10, 'dez') )
    pq.put( (11, 'onze'))
    while( not pq.empty() ):
        print(pq.get(), end= ' ')


#run_test_1()



class Point2D:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    '''
    http://stackoverflow.com/questions/8276983/python-2-and-python-3-cmp 
    def __cmp__(self, point):
        return (self.x < point.x) and (self.y, point.y)
    '''
    '''
    https://docs.python.org/3/reference/datamodel.html#object.__lt__
    '''
    def __lt__ (self, point): # less Than
        return (self.x < point.x) and (self.y, point.y)
    '''
    http://www.rafekettler.com/magicmethods.html
    '''
    def __str__(self):
        return '{x},{y}\n'.format(x=self.x, y=self.y)
    
    def __format__(self, fmt):
        return '{:.2f}{:.2f}'.format(self.x, self.y)
    
def run_test_2():
    pq = PriorityQueue()
    pq.put(Point2D(2,2))
    pq.put(Point2D(-2, -2))
    pq.put(Point2D(2,-10))
    while( not pq.empty() ):
        print(str(pq.get()), end= ' ')
    
run_test_2()
        
if __name__ == '__main__':
    pass