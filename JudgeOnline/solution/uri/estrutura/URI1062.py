'''
Created on May 5, 2016

@author: christoffer
'''
from sys import stdout


'''
https://www.urionlinejudge.com.br/judge/pt/problems/view/1062
Usando STACK
'''

def solution(_list):

        
    return True

#http://stackoverflow.com/questions/529424/traverse-a-list-in-reverse-order-in-python
def print_reverse_list(_list):
    #for i in reversed(_list):
        #stdout.write("%s" % (i))
        
    #for i in _list[::-1]:
        #stdout.write("%s" % (i))
        
    # list comprehension
    stdout.write("%s\n" % ([i for i in _list[::-1]]) )
    obj = ((i, _list[i]) for i in _list[::-1]) 
    print(obj)
    
    
print_reverse_list([1,2,3,4,5])


if __name__ == '__main__':
    pass