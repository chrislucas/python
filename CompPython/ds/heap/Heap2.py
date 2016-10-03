'''
Created on 1 de out de 2016

@author: C.Lucas
'''

class Heap:
    
    def __init__(self, array = [], minmax = 1):
        self._heap = array
        if(len(array) > 0):
            self.minmax = minmax
            self.buildHeap(minmax)
    
    def swap(self, a, b):
        aux = self._heap[a]
        self._heap[a] = self._heap[b]
        self._heap[b] = aux
        
    def validate(self, idx):
        return idx < len(self._heap)
    
    def left(self, idx):
        lf = 2 * idx + 1 
        return lf if self.validate(lf) else -1
            
    def right(self, idx):
        ri = 2 * idx + 2
        return ri if self.validate(ri) else -1
    
    def parent(self, idx):
        idxp = (idx - 1) // 2
        return  idxp if idx != 0 and (self.validate(idxp)) else -1
    
    def add(self, e):
        self._heap.append(e)
        if(self.minmax == 1):
            self.heapifyup(len(self._heap) - 1)
        else:
            self.heapifydown(len(self._heap) - 1)
            
    def getHeap(self):
        return self._heap
    
    
    '''
    maxheap
    '''
    def heapifyup(self, idx):
        idxp = self.parent(idx)
        if(idx >= 0 and idxp >= 0):
            parent = self._heap[idxp]
            current = self._heap[idx]
            if(parent > current):
                self.swap(idx, idxp)
                self.heapifyup(idxp)
    
    def heapifydown(self, idx):
        lf = self.left(idx)
        ri = self.right(idx)
        if(lf > -1 and ri > -1):
            if(self._heap[lf] > self._heap[ri]):
                lf = ri
        if(lf > 0):
            self.swap(idx, lf)
            self.heapifydown(lf)
    
    def minHeap(self, idx):
        lf = self.left(idx)
        ri = self.right(idx)
        if(lf >= 0 and self._heap[lf] < self._heap[idx]):
            _smallest = lf
        else:
            _smallest = idx
        if(ri >= 0 and self._heap[ri] < self._heap[_smallest]):
            _smallest = ri
        if(_smallest != idx):
            self.swap(idx, _smallest)
            self.minHeap(_smallest)
        return None
    
    def maxHeap(self, idx):
        lf = self.left(idx)
        ri = self.right(idx)
        if(lf >= 0 and self._heap[lf] > self._heap[idx]):
            _greatest = lf
        else:
            _greatest = idx
        if(ri >= 0 and self._heap[ri] > self._heap[_greatest]):
            _greatest = ri
        if(_greatest != idx):
            self.swap(idx, _greatest)
            self.maxHeap(_greatest)
        return None
    
    def buildHeap(self, minmax):
        sz = self.size()
        for x in range(sz//2, -1, -1):
            if(minmax == 1):
                self.minHeap(x)
            else:
                self.maxHeap(x)


array2D = [
     [4,5,1,6,7,3,2]
    ,[6,4,5,3,2,0,1]
    ,[8,7,6,3,2,4,5]
    ,[1,4,3,7,8,9,10]
    ,[10,8,9,7,4,1,3]
]

def run():
    heap = Heap(array2D[0], 1)
    print(heap.getHeap())
    
def run2():
    heap = Heap([], 2)
    for x in array2D[2]:
        heap.add(x)
    
    
if __name__ == '__main__':
    pass