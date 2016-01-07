'''
Created on Jan 5, 2016

@author: christoffer
'''
 
'''
In python, a namespace is a mapping from names to objects. Most namespaces are currently
implemented as Python dictionaries.
Examples of namespaces are: the set of built-in names (containing functions such as abs(), and
built-in exception names); the global names in a module, and the local names in a function invocation.
The impportant thing to know about namespaces is that there is abosolutely no relation
between names in different namespaces. For example, two modules may both define a function 'X'
without confusion

Attributes may be read-only or writable. In the latter case, assignment to attributes is possible.
Module attributes are writable. For example: You can write modname.value = 123.
Writable attributes may also be deleted with the del statement (using 'del modname.value'
, Will remove the attribute value from the object named by modname)

There are at least three nested scopes whose namespaces are directly accessible

* The innermost scope, which is searcjed first, contains the local names
* The scope of any enclosing funcions
* The next to last scope contains the current module's global names
* The outermost scope, is the namespace containing built-in names


'''

# union find
class UF:
    elements = []
    
    def __init__(self):
        return
    
    def root(self):
        return
    
    def find(self):
        return


if __name__ == '__main__':
    pass