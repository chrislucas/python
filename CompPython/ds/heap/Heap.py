'''
Created on 9 de ago de 2016

@author: C.Lucas
https://www.hackerearth.com/notes/heaps-and-priority-queues/
http://www.cs.umd.edu/~meesh/351/mount/lectures/lect14-heapsort-analysis-part.pdf
http://quiz.geeksforgeeks.org/binary-heap/
http://www.geeksforgeeks.org/k-ary-heap/
http://www.geeksforgeeks.org/kth-largest-element-in-a-stream/
http://www.geeksforgeeks.org/how-to-check-if-a-given-array-represents-a-binary-heap/
'''

class Heap:
    '''
    classdocs
    '''
    # class attribute. Variavel compartilhada por todas as instancias
    # _heap = []
    
    def __init__(self, array = []):
        '''
        Constructor
        '''
        # instance variable, unique to each instance
        self._heap = array
        self.buildMaxHeap()
    
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
        '''
        idx representa o indice do no raiz do heap
        a formula abaixo aplicasse para idx comecando de 0
        2 * idx + 1 -> no filho a esquerda da raiz
        2 * idx + 2 -> no filho a direita da raiz
        caso idx comece em 1
        2 * idx -> left, 2 * idx + 1 -> right
        [6,4,5,3,2,0,1]
        6 lf:4, ri:5
        4 lf:3, ri:2
        5 lf:0, ri:1
        '''
        lf = 2 * idx + 1
        ri = 2 * idx + 2
        sz = self.size() 
        if(lf <= sz and self._heap[lf] > self._heap[idx]):
            lg = lf
        else:
            lg = idx
        
        if(ri <= sz and self._heap[ri] > self._heap[lg]):
            lg = ri
            
        if(lg != idx):
            self.swap(idx, lg)
            self.maxHeapify(lg)
    
    def buildMaxHeap(self):
        sz = self.size()
        for x in range(sz//2, -1, -1):
            self.maxHeapify(x)
            
    def getHeap(self):
        return self._heap

array = list(range(1, 11))
heap = Heap(array)
print (heap.size(), array)

#print( list(range(10, -1, -1)) )

if __name__ == '__main__':
    pass