'''
Created on Jan 12, 2016

@author: christoffer
'''

# http://www.geeksforgeeks.org/how-to-swap-two-variables-in-one-line/
# ler sobre isso, parece interessante : http://www.geeksforgeeks.org/sequence-points-in-c-set-1/
def swap(a, b):
    a ^= b
    b ^= a
    a ^= b
    return [a, b]


# swap usando bitwise com operador XOR
#msg = "{0}, {1}" .format(a, b)
#msg = "%d %d" % (a, b)
#a ^= b, b ^= a, a ^= b
#print("%d %d %d" % (10 ^ -15, -15 ^ -5, -5 ^ 10))
a = 10
b = 30
a, b = b, a
print( "%d %d" % (a, b) )


#Testando a famosa LIST COMPREHENSION

# uma forma e tranformar a lista numa tupla
msg = "%d,%d" % tuple([int(x) for x in swap(10, -15)])
print (msg)

# iterando sobre a lista, convertendo os itens em string e adicionando uma firgula
msg = (',').join([str(x) for x in swap(10, -15)]) 
print (msg)


if __name__ == '__main__':
    pass