'''
Created on 28 de mai de 2016

@author: C.Lucas
DONE
'''
from sys import stdout, stdin
from math import ceil


m = float(stdin.readline())
p = int(stdin.readline())
t = int(stdin.readline())

#r, s, t = stdin.readline().split(" ")
val = m + ((m*(p/100)) + (m*(t/100)));
if(val - round(val) < 0.5):
    val = round(val)
else :
    val = ceil(val)
    
stdout.write("The total meal cost is %d dollars." % (val) )

if __name__ == '__main__':
    pass