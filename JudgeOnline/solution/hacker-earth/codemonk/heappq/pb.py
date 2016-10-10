'''
Created on 7 de out de 2016

@author: C.Lucas

https://www.hackerearth.com/code-monk-heaps-and-priority-queues/algorithm/monk-and-some-queries/
'''

from sys import stdin, stdout
import heapq
'''
TLE ultimo caso
'''
def solver():
    readLine  = stdin.readline
    writeLine = stdout.write
    cases = int(readLine())
    _heap = []
    while(cases > 0):
        enter = readLine()
        enter = enter.split(' ')
        if(len(enter) > 1):
            op, num = [int(x) for x in enter]
        else:
            op = int(enter[0].rstrip())

        if(op == 1 and num not in _heap):
            heapq.heappush(_heap, num)
            heapq._heapify_max(_heap)
            
        elif(op == 2):
            if num in _heap:
                idx = _heap.index(num)
                _heap.pop(idx)
                heapq._heapify_max(_heap)
            else:
                writeLine('-1\n')

        elif(op == 3 and len(_heap) > 0):
            x = heapq.nlargest(1, _heap)
            writeLine("{:d}\n".format(x[0]))
        
        elif(op == 4 and len(_heap) > 0):
            x = heapq.nsmallest(1, _heap)
            stdout.write("{:d}\n".format(x[0]))
            
        cases -= 1
#solver()

def solver2():
    readLine  = stdin.readline
    writeLine = stdout.write
    cases = int(readLine())
    _map = {}
    Flag = True
    for x in range(0, cases):
        enter = readLine()
        enter = enter.split(' ')
        if(len(enter) > 1):
            op, num = [int(x) for x in enter]
        else:
            op = int(enter[0].rstrip())
            
        if(op == 1):
            if(Flag):
                _min = _max = num
                Flag = False
            elif(num > _max):
                _max = num
            elif(num < _min):
                _min = num
            #if(num in _map):
               # _map[num] += 1
            if(num not in _map):
                _map[num] = True
                
        elif(op == 2):
            if (num in _map):
                #_map.pop(num)
                del _map[num]
                if(len(_map) == 0):
                    Flag = True
                    
                if(num == _max):
                    count = 0
                    for k in _map.keys():
                        if(count == 0):
                            _max = k
                        else:
                            if(k > _max):
                                _max=k
                        count+=1
                                
                if(num == _min):
                    count = 0
                    for k in _map.keys():
                        if(count == 0):
                            _min=k
                        else:
                            if(k < _min):
                                _min=k
                        count+=1
                        
            else:
                writeLine('-1\n')
                
        elif(op == 3):
            writeLine("{}\n".format(_max if len(_map) > 0 else -1))
        
        elif(op == 4):
            writeLine("{}\n".format(_min if len(_map) > 0 else -1))

solver2()

if __name__ == '__main__':
    pass