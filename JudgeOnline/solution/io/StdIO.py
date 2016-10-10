'''
Created on 10 de out de 2016

@author: C.Lucas

https://en.wikibooks.org/wiki/Python_Programming/Input_and_Output
http://stackoverflow.com/questions/22623528/sys-stdin-readline-and-input-which-one-is-faster-when-reading-lines-of-inpu
https://docs.python.org/3/tutorial/inputoutput.html
http://www.python-course.eu/python3_print.php
http://pymbook.readthedocs.io/en/latest/file.html
'''

#_file = open('StdIO', mode='w',  encoding='utf-8')
_file = open('StdIO.bin', mode='w')
#from sys import stderr

'''
format string
https://pyformat.info/
'''

def run_test_input():
    _list = [int(x) for x in input().split(' ')]
    for x in _list:
        #print('%d' % x, sep="?", end=' ', file=stderr)
        #print('{:d}'.format(x), sep="?", end=' ', file=stderr)
        #print('{x}'.format(x=x), sep="?", end=' ', file=stderr)
        #print('{:d}'.format(x), end=' ', file=_file, flush=False)
        #print(bytes('{:d}'.format(x), "utf-8"), end=' ', file=_file, flush=False)
        print(bytes('{}'.format(x), 'utf-8'), end=' ', file=_file, flush=False)
        #_file.write(bytes(x))
        

#print(bytes('{:d}'.format(10), "utf-8"))  
run_test_input()
_file.close()

if __name__ == '__main__':
    pass