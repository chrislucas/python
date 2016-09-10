'''
Created on 8 de set de 2016

@author: chrislucas
'''


'''
bitwise
https://graphics.stanford.edu/~seander/bithacks.html#BitReverseObvious
http://stackoverflow.com/questions/6351374/bitwise-operator-for-simply-flipping-all-bits-in-an-integer
http://marvin.cs.uidaho.edu/Teaching/CS472/bitOps.html
http://www.geeksforgeeks.org/write-an-efficient-c-program-to-reverse-bits-of-a-number/

http://www.geeksforgeeks.org/find-two-missing-numbers-set-2-xor-based-solution/
http://www.catonmat.net/blog/low-level-bit-hacks-you-absolutely-must-know/

Arduino
http://playground.arduino.cc/Code/BitMath
DONE
'''

'''
https://www.hackerrank.com/challenges/flipping-bits
DONE
Dica
Special care should be taken in languages with no unsigned integers to avoid overflows.
'''

from sys import stdin, stdout

'''
flip bit usando operador xor - TOP
http://stackoverflow.com/questions/26065412/flip-bits-using-xor-0xffffffff-or-in-c
Pesquisar por
bit manipulation - Flip bits using XOR 0xffffffff
'''
def flipAllbits(n):
    return n ^  0xffffffff

def flipBists(n):
    return ~n

def run():
    cases = int(stdin.readline())
    while(cases>0):
        n = int(stdin.readline())
        stdout.write("%d\n" % (flipAllbits(n)) )
        cases -= 1


#stdout.write("%d" % (flipAllbits( 0 )) )
run()

if __name__ == '__main__':
    pass