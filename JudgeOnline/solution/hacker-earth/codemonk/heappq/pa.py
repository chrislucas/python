'''
Created on 6 de out de 2016

@author: C.Lucas

https://www.hackerearth.com/code-monk-heaps-and-priority-queues/problems/
https://www.hackerearth.com/code-monk-heaps-and-priority-queues/algorithm/monk-and-multiplication/
'''
from sys import stdin, stdout

'''
Esse problema pede para percorrer o array A
e calcular A[i] * A[i+1] * A[i+2]
'''

class Heap:
    
    def __init__(self, array = []):
        self._heap = array

    def swap(self, a, b):
        aux = self._heap[a]
        self._heap[a] = self._heap[b]
        self._heap[b] = aux
    
    def build(self, sort = 1):
        self.buildMinHeap() if(sort == 1) else self.buildMaxHeap()
       
    def buildMaxHeap(self):
        sz = len(self._heap) - 1
        for x in range(sz//2, -1, -1):
            self.maxHeapify(x, len(self._heap))
    
    def buildMinHeap(self):
        sz = len(self._heap) - 1
        for x in range(sz//2, -1, -1):
            self.minHeapify(x, len(self._heap))
            
    def maxHeapify(self, idx, sz):
        lf = 2 * idx + 1
        ri = 2 * idx + 2
        if(lf < sz and self._heap[lf] > self._heap[idx]):
            largest = lf
        else:
            largest = idx
        if(ri < sz and self._heap[ri] > self._heap[largest]):
            largest = ri
            
        if(largest != idx):
            self.swap(idx, largest)
            self.maxHeapify(largest, sz)
    
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
    
    def getMax(self):
        return self._heap[0]
    
    def add(self, x):
        self.increase(x)
    
    def addIterator(self, data = []):
        for x in data:
            self.add(x)
    
    def increase(self, value):
        self._heap.append(value)
        idx     = len(self._heap)-1
        while(idx > 0 and self._heap[idx//2] < self._heap[idx]):
            self.swap(idx//2, idx)
            idx //= 2
            
    def extractMax(self):
        if(len(self._heap) == 0):
            return -1
        
        x = self._heap[0]
        self._heap[0] = self._heap[len(self._heap)-1]
        self._heap.pop()
        self.maxHeapify(0, len(self._heap))
        return x
      
def solver(nums = []):
    _len = len(nums)
    ans = []
    if(_len > 2):
        heap = Heap()
        heap.addIterator(nums[0:3])
        ans.append(heap._heap[0] * heap._heap[1] * heap._heap[2])
        for x in range(3, _len):
            heap.add(nums[x])
            ans.append(heap._heap[0] * heap._heap[1] * heap._heap[2])
      
    return ans

def test():
    array2D = [
         [4,5,1,6,7,3,2]
        ,[6,4,5,3,2,0,1]
        ,[2,4,3,8,7,6,5]
        ,[4,7,8,3,2,6,5]
        ,[8,7,6,3,2,4,5]
        ,[1,4,3,7,8,9,10]
        ,[10,8,9,7,4,1,3]
        ,[10,8,9,7,6,5,4]
        ,[2,8,5,1,10,5,9,9,3,5]
    ]
    #heap = Heap(array2D[0][:])
    #heap.build(2)
    #print(heap._heap)
    heap = Heap()
    for x in array2D[8][:]:
        heap.add(x)
    print(heap._heap)
    print(heap.extractMax())
    print(heap._heap)
    
def run():
    cases = int(stdin.readline())
    nums = [int(x) for x in stdin.readline().split(' ')]
    ans = solver(nums)
    #print(nums)
    stdout.write("-1\n-1\n")
    for x in ans:
        stdout.write("%d\n" % (x))
#run()
test()



if __name__ == '__main__':
    pass