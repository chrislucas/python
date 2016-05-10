'''
Created on May 2, 2016

@author: christoffer
'''

class Stack(object):
    '''
    classdocs
    '''
    def __init__(self, params):
        '''
        Constructor
        '''
        self.stack = []
        
    def isEmpty(self):
        return self.stack == []
        
    def pop(self):
        return self.stack.pop()
    
    def push(self, item):
        return self.stack.append(item)
    
    def peek(self):
        return self.stack[len(self.stack) - 1]
    
    def size(self):
        return len(self.stack)
    
    
    
if __name__ == 'main':
    pass