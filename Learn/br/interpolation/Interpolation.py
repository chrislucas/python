'''
Created on 31 de dez de 2015

@author: C.Lucas
'''

'''
links sobre string interpolation e operacoes com strings
http://stackoverflow.com/questions/13945749/string-formatting-in-python-3
https://docs.python.org/3.1/library/string.html
''' 
#interpolacao
sfmt = "tamanho de \'{0}\', {1}".format('uma frase qualquer', len('uma frase qualquer')) 
#print(sfmt)
#interpolacao
sfmt = "%d %.2f" % (12, 3.14)
#print(sfmt)

# strings

for char in sfmt:
    print(char, sep=' ', end='')

print("\n%x %o" % (16, 16) )
# preenchimento com 0 a esquerda
print("\n %02d:%03d" % (9,16))

if __name__ == '__main__':
    pass