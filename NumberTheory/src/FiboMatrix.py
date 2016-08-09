'''
Created on 22 de jul de 2016

@author: C.Lucas

https://www.hackerrank.com/challenges/fibonacci-finding-easy
https://en.wikipedia.org/wiki/Fibonacci_number#Matrix_form
https://en.wikipedia.org/wiki/Fibonacci_number
http://www.fullbooks.com/The-first-1001-Fibonacci-Numbers.html
http://tech-queries.blogspot.com.br/2010/09/nth-fibbonacci-number-in-ologn.html
http://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
'''
from sys import stdout, stdin

def fibo(a, b, m):
    mat = [ [b, b], [b, a]]
    aux = [ [b, b], [b, a]]
    i = 1
    while i <= m:
        a1 =  mat[0][0] * aux[0][0] +  mat[0][1] * aux[1][0]
        a2 =  mat[0][0] * aux[0][1] +  mat[0][1] * aux[1][1]
        a3 =  mat[1][0] * aux[0][0] +  mat[1][1] * aux[1][0]
        a4 =  mat[1][0] * aux[0][1] +  mat[1][1] * aux[1][1]
        mat[0][0] = a1
        mat[0][1] = a2
        mat[1][0] = a3
        mat[1][1] = a4
        i+=1
    return mat[1][1]

print(fibo(0,1,1001))

def multiply(mat, cpy, mod):
        a1 =  (((mat[0][0] % mod) * (cpy[0][0] % mod) % mod) +  ((mat[0][1] % mod) * (cpy[1][0] % mod) % mod)) % mod
        a2 =  (((mat[0][0] % mod) * (cpy[0][1] % mod) % mod) +  ((mat[0][1] % mod) * (cpy[1][1] % mod) % mod)) % mod
        a3 =  (((mat[1][0] % mod) * (cpy[0][0] % mod) % mod) +  ((mat[1][1] % mod) * (cpy[1][0] % mod) % mod)) % mod
        a4 =  (((mat[1][0] % mod) * (cpy[0][1] % mod) % mod) +  ((mat[1][1] % mod) * (cpy[1][1] % mod) % mod)) % mod
        mat[0][0] = a1
        mat[0][1] = a2
        mat[1][0] = a3
        mat[1][1] = a4

def powmat(mat, cpy, exp, mod):
    if(exp == 0 or  exp == 1):
        return None
    powmat(mat, cpy, exp//2, mod)
    multiply(mat, mat, mod)
    if(exp%2!=0):
        multiply(mat, cpy, mod)
    return  None  

def powmat2(mat, cpy, exp, mod):
    if(exp == 0 or  exp == 1):
        return None
    while(exp > 1):
        multiply(mat, mat, mod)
        if(exp%2==0):
            exp //= 2
        else:
            multiply(mat, cpy, mod)
            exp = (exp-1)//2
    return None
           
def solver3(a, b, m, mod):
    mat = [ [b, b], [b, a]]
    cpy = [ [b, b], [b, a]]
    powmat(mat, cpy, m, mod)
    return mat[1][1]

def solver4(a, b, m, mod):
    mat = [ [b, b], [b, a]]
    cpy = [ [b, b], [b, a]]
    powmat2(mat, cpy, m, mod)
    return mat[1][1]

# https://pt.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/modular-addition-and-subtraction
def solver(a, b, m, mod):
    mat = [ [b, b], [b, a]]
    cpy = [ [b, b], [b, a]]
    i = 1
    while i <= m:
        multiply(mat, cpy, mod)
        i+=1
    return mat[1][1]

def solver2(a, b, m, mod):
    while m > 1:
        aux = (a%mod + b%mod) % mod
        a = b
        b = aux
        m-=1
    return b

def runTest():
    a = solver(0,1,40,1000000007)
    b = solver2(0,1,40,1000000007)
    c = solver3(0,1,40,1000000007)
    d = solver4(0,1,40,1000000007)
    stdout.write("a:%d,b:%d,c:%d,d:%d" % (a, b, c, d))
#runTest()

def run():
    cases = int(stdin.readline())
    while cases > 0:
        enter = stdin.readline().rstrip().split(' ')
        a,b,n = [int(x) for x in enter]
        ans = solver(a,b,n,1000000007)
        stdout.write("%d\n" % (ans))
        cases -=1 
run()

if __name__ == '__main__':
    pass