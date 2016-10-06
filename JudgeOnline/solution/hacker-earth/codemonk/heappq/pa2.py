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
'''


import heapq
from sys import stdin, stdout

def solver(nums = []):
    _len = len(nums)
    ans = []
    if(_len > 2):
        array = []
        heapq.heappush(array, nums[0])
        heapq.heappush(array, nums[1])
        heapq.heappush(array, nums[2])
        heapq._heapify_max(array)
        ans.append(array[0] * array[1] * array[2])
        for x in range(3, _len):
            heapq.heappush(array, nums[x])
            heapq._heapify_max(array)
            pq = heapq.nlargest(3, array)
            #print(pq)
            ans.append(pq[0] * pq[1] * pq[2])
    return ans

def run():
    cases = int(stdin.readline())
    nums = [int(x) for x in stdin.readline().split(' ')]
    ans = solver(nums)
    stdout.write("-1\n-1\n")
    for x in ans:
        stdout.write("%d\n" % (x))
run()

if __name__ == '__main__':
    pass