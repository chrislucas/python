'''
Created on 11 de dez de 2016

@author: C.Lucas
https://www.hackerrank.com/challenges/linear-algebra-foundations-3-matrix-multiplication
DONE
'''

# http://stackoverflow.com/questions/2397141/how-to-initialize-a-two-dimensional-array-in-python
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


a = [ [1,2], [2,3] ]
b = [ [4,5], [7,8] ]

#https://www.hackerrank.com/challenges/linear-algebra-foundations-4-matrix-multiplication?h_r=next-challenge&h_v=zen
# DONE
a = [ [1,2,3], [2,3,4], [1,1,1]]
b = [ [4,5,6], [7,8,9], [4,5,7]]

#multiply(a, b)


# https://www.hackerrank.com/challenges/linear-algebra-foundations-5-the-100th-power-of-a-matrix?h_r=next-challenge&h_v=zen
# DONE
def run():
    origin = [ [1,1,0], [0,1,0], [0,0,1]]
    # http://stackoverflow.com/questions/6532881/how-to-make-a-copy-of-a-2d-array-in-python
    a = [row[:] for row in origin]
    for x in range(99):
        a = multiply(origin, a)
    return a
run()
#print(*range(1))

if __name__ == '__main__':
    pass