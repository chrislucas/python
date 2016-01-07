'''
Created on Jan 7, 2016

@author: christoffer
'''

# https://www.hackerrank.com/challenges/quicksort2

def swap(array, i, j):
    aux = array[i]
    array[i] = array[j]
    array[j] = aux

def partition(arraym lf, ri):
    return 

def quicksort(array, lf, ri):
    
    if(lf >= ri)
        return
    
    pivot = array[0]
    
    part = partition(array, lf, ri)
    quicksort(array, lf, part-1)
    quicksort(array, part+1, ri)


def main():
    from sys import stdin, stdout
    sz      = stdin.readline()
    array   = [int(i) for i in stdin.readline().strip().split()]
    quicksort(array, 0, sz-1)
    stdout.write(str(array))
    
if __name__ == '__main__':
    main()    