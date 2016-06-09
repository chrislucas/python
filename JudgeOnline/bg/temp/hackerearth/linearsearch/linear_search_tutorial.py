'''
Created on Jun 9, 2016

@author: christoffer
https://www.hackerearth.com/practice/algorithms/searching/linear-search-1/tutorial/
DONE
'''
from sys import stdout, stdin

def solution(array, M):
    maxIdx = -1
    for i in range(0, len(array)):
        if(array[i] == M and i > maxIdx):
            maxIdx = i
    stdout.write("%d\n" % (maxIdx + 1))
    
def run():
    s, m    = [x for x in stdin.readline().split(" ")]
    s, m    = [int(s), int(m)]
    array   = [int(x) for x in stdin.readline().split(" ")]
    solution(array, m)

run()
    
if __name__ == '__main__':
    pass