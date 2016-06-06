'''
Created on 28 de mai de 2016

@author: C.Lucas
DONE
'''
from sys import stdout, stdin


def S():
    N = int(stdin.readline())
    if(N%2>0):
        stdout.write("Weird")
    elif(N%2==0 and N >= 2 and N <= 5):
        stdout.write("Not Weird")
    elif(N%2==0 and N >= 6 and N <= 20): 
        stdout.write("Weird")
    elif(N%2==0 and N > 20):
        stdout.write("Not Weird")
S()

if __name__ == '__main__':
    pass