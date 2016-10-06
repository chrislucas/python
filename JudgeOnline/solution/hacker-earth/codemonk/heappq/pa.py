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
    
    def add(self, x):
        self.increase(len(self._heap), x)
        return None
       
    def buildMaxHeap(self):
        sz = self.size()
        for x in range(sz//2, -1, -1):
            self.maxHeapify(x, len(self._heap))
    
    def buildMinHeap(self):
        sz = self.size()
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
            
        if(lg != idx):
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
    
    def increase(self, idx, value):
        self._heap[idx] = value
        while(idx > 0 and self._heap[idx//2] < self._heap[idx]):
            swap(idx//2, idx)
            idx //= 2
        return None
      
def solver(nums = []):
    _len = len(nums)
    ans = []
    if(_len > 2):
        heap = Heap()
        heap.add(nums[0])
        heap.add(nums[1])
        heap.add(nums[2])
        heap.buildMaxHeap()
        for x in range(3, _len):
            x
        
    return ans
    
def run():
    cases = int(stdin.readline())
    nums = [int(x) for x in stdin.readline().split(' ')]
    ans = solver(nums)
    #print(nums)
    stdout.write("-1\n-1\n")
    for x in ans:
        stdout.write("%d\n" % (x))
run()


if __name__ == '__main__':
    pass