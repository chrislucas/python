'''
Created on 11 de dez de 2016

@author: C.Lucas
https://www.hackerrank.com/challenges/linear-algebra-foundations-7-the-1000th-power-of-a-matrix?h_r=next-challenge&h_v=zen
DONE
'''
def multiply(a, b):   
    l = len(a)
    c = len(b[0])
    #ans = [ [0] * l, [0] * c]
    #ans = [[0] * l] * c
    #ans = [x[:] for x in [[0] * l] * c]
    ans = [[0 for x in range(c)] for y in range(l)]
    if(l != c):
        return ans
    for i in range(0, l):
        for j in range(0, c):
            for k in range(0, l):
                ans[i][j] += a[i][k] *  b[k][j]
    return ans

def run():
    origin = [ [-2,-9], [1, 4]]
    # http://stackoverflow.com/questions/6532881/how-to-make-a-copy-of-a-2d-array-in-python
    a = [row[:] for row in origin]
    for x in range(999):
        a = multiply(origin, a)
    return a
run()
if __name__ == '__main__':
    pass