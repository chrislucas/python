'''
Created on 18 de mai de 2016

@author: C.Lucas
'''

'''
https://docs.python.org/3/tutorial/controlflow.html
'''
'''
arbitrary arguments
'''
def arbitrary_args (*args, _str='/'):
    return _str.join(args)

print(arbitrary_args('comp', 'io', 'files', 'hack'))

if __name__ == '__main__':
    pass