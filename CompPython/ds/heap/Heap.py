'''
Created on 9 de ago de 2016

@author: C.Lucas
https://www.hackerearth.com/notes/heaps-and-priority-queues/
http://quiz.geeksforgeeks.org/binary-heap/
http://www.geeksforgeeks.org/k-ary-heap/
http://www.geeksforgeeks.org/kth-largest-element-in-a-stream/
http://www.geeksforgeeks.org/how-to-check-if-a-given-array-represents-a-binary-heap/
'''

class Heap(object):
    '''
    classdocs
    '''
    # class attribute
    _heap = []
    
    def __init__(self, array = []):
        '''
        Constructor
        '''
        _heap = array
        return None
    
    '''
        Max heap: o valor do no Pai na arvore binaria completa eh maior
        que os valores dos nos filhos a esquerda e a direita
    '''
   
    def size(self):
        return len(self._heap)
   
    def swap(self, a, b):
        aux = self._heap[a]
        self._heap[a] = self._heap[b]
        self._heap[b] = aux
        
    # metodo para manter a propriedade de maxheap
    def maxHeapify(self, idx):
        lf = 2 * idx
        ri = 2 * idx + 1
        sz = self.size() 
        if(lf <= sz and self._heap[lf] > self._heap[idx]):
            lg = lf
        else:
            lg = idx
        
        if(ri <= sz and self._heap[ri] > self._heap[lg]):
            lg = ri
            
        if(lg != idx):
            self.swap(idx, lg)
            self.maxHeappify(lg)
    
    def buildMaxHeap(self):
        sz = self.size()
        for x in range(sz//2, 0, -1):
            x


if __name__ == '__main__':
    pass