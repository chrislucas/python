'''
Created on Jun 9, 2016

@author: christoffer
https://en.wikipedia.org/wiki/Longest_increasing_subsequence
http://www.geeksforgeeks.org/dynamic-programming-set-3-longest-increasing-subsequence/
https://a2oj.com/category?ID=79
http://www.algorithmist.com/index.php/Longest_Increasing_Subsequence
https://www.hackerrank.com/challenges/longest-increasing-subsequent
'''

# Van der Corput sequence https://en.wikipedia.org/wiki/Van_der_Corput_sequence
van_seq = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
instance = [
    [ 1, 12, 7, 0, 23, 11, 52, 31, 61, 69, 70, 2 ]
]

def naiveTopDown(array, sz):
    
    if(sz == 1):
        return 1
    

def bottomUp(array):
    sz  = len(array)
    lis = [0] * sz
    for i in range(0, sz):
        _max = -1
        for j in range(0, i):
            if(array[i] > array[j]):
                if(_max == -1 or _max < lis[j] + 1):
                    _max = 1 + lis[j]
        
        lis[i] = _max if _max > -1 else 1
    
        ans = [int] * 2
        acc = 0
        for idx in range(0, sz):
            if(acc < lis[idx]):
                ans[0] = idx
                ans[1] = lis[idx]
                acc = lis[idx]
        
        return ans

bottomUp(van_seq)
print(0x0f)
    
if __name__ == '__main__':
    pass