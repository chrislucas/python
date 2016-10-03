'''
Created on Apr 26, 2016

@author: christoffer
'''
'''
data structure
https://docs.python.org/3/tutorial/datastructures.html

Queue
https://docs.python.org/3/library/queue.html


heappq
https://docs.python.org/3/library/heapq.html

http://stackoverflow.com/questions/9289614/how-to-put-items-into-priority-queues
http://stackoverflow.com/questions/21768493/python3-queue-priorityqueue-changes
https://docs.python.org/3/library/queue.html
'''

from collections import deque
from queue import PriorityQueue
import queue


class Data:
    def __init__(self, value):
        self.value = value


def usePQ():

    queue = PriorityQueue()
    queue.put((10, 'dez'))
    queue.put((8, 'oito'))
    queue.put((9, 'nove'))
    

    queue = PriorityQueue()
    queue.put((1, Data(10)))
    queue.put((3, Data(30)))
    queue.put((2, Data(20)))
    
    while not queue.empty() :
        print("%d %s" % queue.get())

    

def useDq():
    print( deque( ['A', 'C', 'D'] ) )

useDq()
usePQ()



    
    
if __name__ == '__main__':
    pass