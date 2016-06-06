'''
Created on 28 de mai de 2016

@author: C.Lucas
DONE
'''
i = 4
d = 4.0
s = 'HackerRank '

from sys import stdout, stdin;

ii = int(stdin.readline())
dd = float(stdin.readline())
ss = stdin.readline()

# https://wiki.python.org/moin/PythonSpeed/PerformanceTips#String_Concatenation
stdout.write("%d\n%.1f\n%s%s" % (ii+i, dd+d, s, ss))

if __name__ == '__main__':
    pass