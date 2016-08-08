'''
Created on 25 de jul de 2016

@author: C.Lucas
artigo cita mais leituras dentro dele
https://bosker.wordpress.com/2011/07/27/computing-fibonacci-numbers-using-binet%E2%80%99s-formula/

http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibFormula.html
https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Fibonacci_Number_Program#Using_Binet.27s_formula
https://artofproblemsolving.com/wiki/index.php?title=Binet%27s_Formula

binet formula and sucessor formula
http://jwilson.coe.uga.edu/emat6680/parveen/Fib_Numbers.htm
'''
from math import sqrt

'''
problems
https://www.hackerrank.com/challenges/fibonacci-finding-easy/topics/fibonacci-numbers
https://www.hackerrank.com/challenges/is-fibo/topics/binets-formula
https://www.hackerrank.com/challenges/is-fibo
https://www.hackerrank.com/challenges/fibonacci-finding-easy/topics
'''

'''
exp fast
decima sexta vez escrevendo esse metodo denovo
https://en.wikipedia.org/wiki/Exponentiation_by_squaring
https://discuss.codechef.com/questions/20451/a-tutorial-on-fast-modulo-multiplication-exponential-squaring
'''

def fexp1(b, e):
    if(e == 0):
        return 1
    elif(e == 1):
        return b
    elif(e < 0):
        e = -e
        b = 1/b
    acc = 1.0
    while(e>1):
        if(e % 2 == 0):
            e //= 2
        else:
            acc *= b
            e = (e-1)//2
        b *= b
    return acc * b

def biner_formula(n):
    s = sqrt(5)
    p = (1 + s) / 2 # phi
    m = (fexp1(p, n) + fexp1(1-p, n)) / s
    return round(m)

print(biner_formula(79))

if __name__ == '__main__':
    pass