'''
Created on 12 de nov de 2016

@author: C.Lucas
https://www.hackerrank.com/challenges/basic-probability-puzzles-7/submissions/code/32133629
'''

A = 500
B = 1000
C = 2000
T = A+B+C
EA = 0.005
EB = 0.008
EC = 0.010
PA = A/T
PB = B/T
PC = C/T
'''
1/7 * 1/200 + 2/7 * 1/125 + 4/7 * 1/100
1/1400 + 2/875 + 4/700 = 61/7000
1/1400 / 61/7000 = 7000/85400 simplificando por 1400 = 5/61
'''
PE = (PA * EA) + (PB * EB) + (PC * EC)
print((PA * EA)/ PE)

if __name__ == '__main__':
    pass