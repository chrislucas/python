'''
Created on May 4, 2016

@author: christoffer
'''

'''
Sobre sequence unpacking python 3

https://www.python.org/dev/peps/pep-3132/
http://stackoverflow.com/questions/6967632/unpacking-extended-unpacking-and-nested-extended-unpacking
http://stackoverflow.com/questions/33956772/extended-sequence-unpacking-in-python3

procurar sequence unpacking
https://docs.python.org/3.3/tutorial/datastructures.html

http://openbookproject.net/thinkcs/python/english3e/tuples.html
http://www.java2s.com/Tutorials/Python/Statement/What_is_sequence_unpacking_in_Python.htm

'''

from sys import stdout

seq = [1,2,3,5]

a,b,c,d = seq

stdout.write("%d %d %d %d" % (a,b,c,d) )

if __name__ == '__main__':
    pass