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
    
    def maxHeapify(self, idx, sz):
        lf = 2 * idx + 1
        ri = 2 * idx + 2
        
        if(lf < sz and self._heap[lf] > self._heap[idx]):
            _greatest= lf
        else:
            _greatest = idx
        if(ri < sz  and self._heap[ri] > self._heap[_greatest]):
            _greatest = ri
        if(_greatest != idx):
            self.swap(idx, _greatest)
            self.maxHeapify(_greatest, sz)
            
            
    def minHeapify(self, idx, sz):
        lf = 2 * idx + 1
        ri = 2 * idx + 2
        if(lf < sz and self._heap[lf] < self._heap[idx]):
            _smallest = lf
        else:
            _smallest = idx
        if(ri < sz  and self._heap[ri] < self._heap[_smallest]):
            _smallest = ri
        if(_smallest != idx):
            self.swap(idx, _smallest)
            self.minHeapify(_smallest, sz)
            
    def buildMaxHeap(self):
        sz = len(self._heap) - 1
        for x in range(sz//2, -1, -1):
            self.maxHeapify(x, len(self._heap))
    
    def buildMinHeap(self):
        sz = len(self._heap) - 1
        for x in range(sz//2, -1, -1):
            self.minHeapify(x, len(self._heap))
    
    def sort(self, order = 2):
        '''
            usando a propriedade do heapmax ordenamos em ASC, com 
            heapmin ordenamos em DESC
        '''
        self.buildMaxHeap() if(order == 2) else self.buildMinHeap()     
        sz  = len(self._heap)
        lim = sz - 1
        for x in range(lim, 0, -1):
            '''
                trocamos o primeiro elemento com o ultimo
            '''
            self.swap(0, x)
            '''
                diminuimos o tamanho do heap excluindo o ultimo
                elemento, garantindo que ele nao seja alterado
            '''
            sz -= 1
            if(order == 2):
                self.maxHeapify(0, sz)
            else:
                self.minHeapify(0, sz)
                
    def getHeap(self):
        return self._heap
    
    def maxE(self):
        return self._heap[0]
    
    def minE(self):
        return self._heap[len(self._heap)-1]
    
    def extractMax(self):
        if(len(self._heap) > 0):
            _max = self._heap[0]
            _len = len(self._heap)
            self._heap[0] = self._heap[_len-1]
            self.maxHeapify(0, _len)
            return _max
        else:
            return -1
    
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
#print(heap.getHeap())
heap.sort()
print(heap.getHeap())


if __name__ == '__main__':
    pass
        