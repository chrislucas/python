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
#import copy

class Heap:
    '''
    classdocs
    '''
    # class attribute. Variavel compartilhada por todas as instancias
    # _heap = []
    
    def __init__(self, array = [], _type = 1):
        '''
        Constructor
        '''
        # instance variable, unique to each instance
        self._heap = array   
        if(_type == 1):
            self.buildMinHeap()
        else:
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
    
    '''
        o metodo validade Idx eh simples porem util
        pois concentra num unico ponto a validacao de
        indices validos do heap
        usamos o operador '<' quando contanos de 0 a N
        e podemos mudar para '<=' quando lidarmos com 1 a n+1 
    '''
    def validate(self, idx):
        return idx < len(self._heap)
    '''
        Os metodos left, right e parent
        foram construidos para arrays[0..n]
        para arrays[1..N+1] rever a logica
    '''
    def left(self, idx):
        lf = 2 * idx + 1 
        return lf if self.validate(lf) else -1
            
    def right(self, idx):
        ri = 2 * idx + 2
        return ri if self.validate(ri) else -1
    
    def parent(self, idx):
        idxp = (idx - 1) // 2
        return  idxp if idx != 0 and (self.validate(idxp)) else -1
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
        lf = self.left(idx)  #2 * idx + 1
        ri = self.right(idx) #2 * idx + 2
        '''
            verifica se  o no a esquerda tem um valor maior
            que o do no pai
            se simpega o indice do no da esquerd
        '''
        if(lf>-1 and self._heap[lf] > self._heap[idx]):
            lg = lf
        else:
            # se map foca com o indice do no pai mesmo
            lg = idx
        '''
            verifica se  o no a direita tem um valor maior
            que o do no (pai ou da esquerda, depende
            do que acontecer no condicional acima)
        '''
        if(ri>-1 and self._heap[ri] > self._heap[lg]):
            lg = ri
            
        if(lg != idx):
            self.swap(idx, lg)
            self.maxHeapify(lg)
    
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
        sz = self.size()
        for x in range(sz//2, -1, -1):
            self.maxHeapify(x)
    
    def buildMinHeap(self):
        sz = self.size()
        for x in range(sz//2, -1, -1):
            self.minHeapify(x)
    
    def heapsort(self, order = 1):
        if(order == 1):
            self.buildMinHeap()
        else:
            self.buildMaxHeap()
        return None
            
    def getHeap(self):
        return self._heap

array2D = [
     [4,5,1,6,7,3,2]
    ,[6,4,5,3,2,0,1]
    ,[4,7,8,3,2,6,5]
    ,[8,7,6,3,2,4,5]
    ,[1,4,3,7,8,9,10]
    ,[10,8,9,7,4,1,3]
]

'''
nao funciona para lista com mais de 1D
_copy = list(array[0][:]) #copy.deepcopy(array[0][:])
print(_copy)

http://henry.precheur.org/python/copy_list

Copiar array2D
[x[:] for x in array2D]

'''

#_copy = [x[:] for x in array2D]
#print(id(array2D), id(_copy))

# passando uma copia do array, nao a referencia
heap = Heap(array2D[2][:], 2)
print (heap.size(), array2D[2], heap.getHeap())

#print( list(range(10, -1, -1)) )

if __name__ == '__main__':
    pass