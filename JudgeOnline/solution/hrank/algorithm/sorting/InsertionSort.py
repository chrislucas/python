'''
Created on May 16, 2016

@author: christoffer

https://en.wikipedia.org/wiki/Insertion_sort
https://pt.wikipedia.org/wiki/Insertion_sort

Problema
https://www.hackerrank.com/challenges/insertion-sort

'''

def swap(_list, i, j):
    aux = _list[i]
    _list[i] = _list[j]
    _list[j] = aux

def insertionSortV1(_list):
    for i in range(1, len(_list), 1):
        e = _list[i]
        j = i-1
        while(j>=0 and e < _list[j]):
            _list[j+1] = _list[j]
            j -= 1
        #j for diferente de i-1, houve troca
        if(j != i-1):
            _list[j+1] = e
    print(_list)

def insertionSortV2(_list):
    counter = 0
    for i in range(1, len(_list)):
        j = i
        while(j > 0 and _list[j-1] > _list[j]):
            counter += 1
            swap(_list, j-1, j)
            j -= 1
    #print(_list)        
    return counter

#insertionSortV1([5,2,3,4,1])
#insertionSortV2([5,2,3,4,1])
#insertionSortV2([5,4,3,2,1])
#insertionSortV2([1,5,3,2,4])
#insertionSortV2([1,4,3,2,5])


if __name__ == '__main__':
    pass