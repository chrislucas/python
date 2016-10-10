'''
Created on 6 de out de 2016

@author: C.Lucas

https://docs.python.org/3/library/heapq.html
'''

array2D = [
     [4,5,1,6,7,3,2]
    ,[6,4,5,3,2,0,1]
    ,[2,4,3,8,7,6,5]
    ,[4,7,8,3,2,6,5]
    ,[8,7,6,3,2,4,5]
    ,[1,4,3,7,8,9,10]
    ,[10,8,9,7,4,1,3]
    ,[10,8,9,7,6,5,4]
]

import heapq


'''
http://stackoverflow.com/questions/2501457/what-do-i-use-for-a-max-heap-implementation-in-python
'''

'''
http://stackoverflow.com/questions/33024215/built-in-max-heap-api-in-python
'''
class Neg:
    def __init__(self, x):
        self.x = x
    
    '''
    https://docs.python.org/3.0/whatsnew/3.0.html
    '''
    def __cmp__(self, obj):
        #return cmp(self.x, obj.x)
        return None

def test_heapify_min_max():
    _copy = array2D[0][:]
    print(_copy)
    #heapq.heapify(_copy)
    heapq._heapify_max(_copy)
    print(_copy)
    
#test_heapify_min_max()


def _heapsort(array):
    _arr = []
    for x in array:
        heapq.heappush(_arr, x)
    # list comprehesion
    # [heapq.heappop(_arr) for i in range(len(_arr))]
    ans = []
    i = 0
    while i < len(_arr):
        x = heapq.heappop(_arr)
        ans.append(x)
        
    return  ans

print(_heapsort([0,3,1,2,-5,0]))

def test_s():
    return None


if __name__ == '__main__':
    pass