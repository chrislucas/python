'''
Created on May 17, 2016

@author: christoffer
'''
import os

'''
Arrays
http://www.i-programmer.info/programming/python/3942-arrays-in-python.html
http://www.i-programmer.info/programming/python/3942-arrays-in-python.html?start=1
http://stackoverflow.com/questions/27760831/assigning-values-to-an-array-with-for-loop-python
'''

def initialize_array_1d(M = 1):
    array_list = [None] * M
    return array_list

def initialize_array_2d(M = 1, N = 1):
    array_list = []
    i = 0
    while i < M: 
        array_list.append([None] * N)
        i+=1
    return array_list

def read_file_v1():
    path = os.path.join(os.path.dirname(__file__), '../files/grid.txt')
    print(__file__)
    print(os.path.dirname(__file__))
    print(path)
    try:
        with open(path, mode='r') as FileObject:
            for lines in FileObject:
                #print(type(lines))
                print(lines)
    except IOError:
        print('Erro ao ler o arquivo')
    return None

def write_file():
    return None

'''
Statements
https://docs.python.org/3/reference/compound_stmts.html

With
http://preshing.com/20110920/the-python-with-statement-by-example/
http://effbot.org/zone/python-with-statement.htm
http://stackoverflow.com/questions/1369526/what-is-the-python-keyword-with-used-for
https://docs.python.org/3.1/reference/compound_stmts.html
http://preshing.com/20110920/the-python-with-statement-by-example/
'''

'''
print(type(False))
print(type(None))
print(initialize_array_1d(10))
print(initialize_array_2d(2, 3))
'''

read_file_v1()


if __name__ == '__main__':
    pass