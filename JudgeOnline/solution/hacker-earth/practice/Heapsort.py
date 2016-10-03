'''
Created on 3 de out de 2016

@author: chrislucas

https://www.hackerearth.com/practice/algorithms/sorting/heap-sort/tutorial/
https://www.hackerearth.com/practice/notes/heaps-and-priority-queues/
'''

class Heapsort():
    '''
    classdocs
    '''
    def __init__(self, array = []):
        '''
        Constructor
        '''
        self._heap = array

    
    def add(self, e):
        return None
    
    def removeMin(self):
        return None
    
    def getMin(self):
        return None
    
    def getMax(self):
        return None
    
    def build(self, sort):
        if(sort == 1):
            self.buildMinHeap()
        elif(sort == 2):
            self.buildMaxHeap()
    
    def validate(self, idx):
        return idx < len(self._heap)
    
    def swap(self, a, b):
        aux = self._heap[a]
        self._heap[a] = self._heap[b]
        self._heap[b] = aux
    
    def left(self, idx):
        lf = 2 * idx + 1 
        return lf if self.validate(lf) else -1
            
    def right(self, idx):
        ri = 2 * idx + 2
        return ri if self.validate(ri) else -1
    
    def parent(self, idx):
        idxp = (idx - 1) // 2
        return  idxp if idx != 0 and (self.validate(idxp)) else -1  
    
    def maxHeapify(self, idx):
        lf = self.left(idx)
        ri = self.right(idx)
        if(lf >= 0 and self._heap[lf] > self._heap[idx]):
            _greatest= lf
        else:
            _greatest = idx
        if(ri >= 0  and self._heap[ri] > self._heap[_greatest]):
            _greatest = ri
        if(_greatest != idx):
            self.swap(idx, _greatest)
            self.maxHeapify(_greatest)
            
            
    def minHeapify(self, idx):
        lf = self.left(idx)
        ri = self.right(idx)
        if(lf >= 0 and self._heap[lf] < self._heap[idx]):
            _smallest = lf
        else:
            _smallest = idx
        if(ri >= 0  and self._heap[ri] < self._heap[_smallest]):
            _smallest = ri
        if(_smallest != idx):
            self.swap(idx, _smallest)
            self.minHeapify(_smallest)
            
    def buildMaxHeap(self):
        sz = len(self._heap)
        for x in range(sz//2, -1, -1):
            self.maxHeapify(x)
    
    def buildMinHeap(self):
        sz = len(self._heap)
        for x in range(sz//2, -1, -1):
            self.minHeapify(x)
    
    def sort(self, order = 1):
        if(order == 1):
            self.buildMinHeap()
        else:
            self.buildMaxHeap()
        '''
            apos montar o heap, seja maximo ou minimo
            o primeiro elemento sera o maiour caso for montado o heapmax
            ou o menor do array caso contrario
        '''    
        sz = len(self._heap) - 1
        for x in range(sz, 1, -1):
            self.swap(0, x)
            if(order == 1):
                self.minHeapify(x)
            else:
                self.maxHeapify(x)
                
    def getHeap(self):
        return self._heap
    
array2D = [
     [4,5,1,6,7,3,2]
    ,[4,3,7,1,8,5]
    ,[6,4,5,3,2,0,1]
    ,[4,7,8,3,2,6,5]
    ,[8,7,6,3,2,4,5]
    ,[8,4,7,1,3,5]
    ,[1,4,3,7,8,9,10]
    ,[10,8,9,7,4,1,3]
    ,[10,8,9,7,6,5,4]
]

heap = Heapsort(array2D[1][:])
print(heap.getHeap())
heap.sort(1)
print(heap.getHeap())


if __name__ == '__main__':
    pass
        