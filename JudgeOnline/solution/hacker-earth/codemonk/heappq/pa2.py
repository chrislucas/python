'''
Created on 6 de out de 2016

@author: chrislucas

uso interessante da heapq
https://www.safaribooksonline.com/library/view/python-cookbook-3rd/9781449357337/ch01s04.html
http://stackoverflow.com/questions/3139869/heapq-nlargest-index-of-returned-result-in-original-sequence
https://docs.python.org/3/library/heapq.html
'''

'''
Problem
https://www.hackerearth.com/code-monk-heaps-and-priority-queues/algorithm/monk-and-multiplication/
Essa solucao da TLE no ultimo caso a entrada tem 100000 numeros

DONE sem o uso de heapq
'''


import heapq
from sys import stdin, stdout

def solver(nums = []):
    _len = len(nums)
    if(_len > 2):
        array = []
        heapq.heappush(array, nums[0])
        heapq.heappush(array, nums[1])
        heapq.heappush(array, nums[2])
        #heapq._heapify_max(array)
        stdout.write("%d\n" % (array[0] * array[1] * array[2]))
        for x in range(3, _len):
            heapq.heappush(array, nums[x])
            #heapq._siftup_max(array, 0)
            pq = heapq.nlargest(3, array)
            stdout.write("%d\n" % (pq[0] * pq[1] * pq[2]))

def run():
    cases = int(stdin.readline())
    nums = [int(x) for x in stdin.readline().split(' ')]
    stdout.write("-1\n-1\n")
    solver(nums)

# http://stackoverflow.com/questions/33024215/built-in-max-heap-api-in-python
def _heappush_max(heap, item):
    heap.append(item)
    #heapq._siftdown_max(heap, 0, len(heap)-1)
    #heapq._heapify_max(x)

def sort3idx(array):
    if(array[0] <  array[1]):
        aux = array[0]
        array[0] = array[1]
        array[1] = aux
    
    if(array[1] <  array[2]):
        aux = array[1]
        array[1] = array[2]
        array[2] = aux
    
    if(array[0] <  array[1]):
        aux = array[0]
        array[0] = array[1]
        array[1] = aux
# passou mano
def run2():
    cases = int(stdin.readline())
    nums = [int(x) for x in stdin.readline().split(' ')]
    array = []
    for idx in range(0, len(nums)):
        array.append(nums[idx])
        if(idx < 2):
            stdout.write("-1\n")
            continue
        if(len(array) > 3):
            if(array[2] < array[3]):
                array[2] = array[3]
            array.pop()
        sort3idx(array)
        stdout.write("%d\n" % (array[0] * array[1] * array[2]))
        
run2()

if __name__ == '__main__':
    pass