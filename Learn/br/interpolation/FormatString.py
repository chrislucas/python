'''
Created on 31 de dez de 2015

@author: C.Lucas
'''
from builtins import len

'''
mapa = [('Page', 'Guitar', 'Led Zeppelin')
       ,('Fripp', 'Guitar', 'K. C.')]

for name, instrument, band in mapa:
    print('{0}, {1}, {2}'.format(name, instrument, band), end='\n',  flush=True)
'''
# outra forma de for
#print ('{saudacao}'.format(saudacao='Ola mundo'))

# funcao interna para formatacao
# print(format(3.1415, '.3e'))


# uso de colchetes para pegar uma substring
# chamado de slice
msg = 'aisjdaisjdaidjasdkasjdlakjdlaskjdlaksjdlasdj'
# string[inicio, fim, intervalo]
# string[::-1] imprime a string invertida
print ( '%s\n%s\n%s\n%s\n%s' % (msg[2:10],msg[:2]
                                ,msg[-len(msg)::]
                                ,msg[1::3]
                                ,msg[::-1]) )


if __name__ == '__main__':
    pass