'''
Created on May 20, 2016

@author: christoffer
'''


def solIterative(p, j):
    s = 1
    for i in (1, p+1):
		'''
		 i+j representa o salto partindo da i-esima pessoa
		 o -1 eh um 'ajuste', pois quando vc realiza um salto
		 a partir da i-esima pessoa por exemplo i=1, um salto
		 k = 3 deveria nos levar a 3ª pessoa, mas i+3=4. Entao fazemos o ajusto
		 No final da formula temos (modulo p + 1) o modulo p e para quando chegarmos
		 ao fn]inal da fila circular, assim podemos recomeçar a contagem e o +1 eh um novo 'ajusto'
		 Esse ajusta trata a retirada da i-esima pessoa da contagem. Lembrando, fizemos
		 um salto k, retiramos o elemento i+k-1 da fila, agora temos que contar a partir do
		 proximo elemento. Exemplo p = 5, k = 2
		 no primeiro salto, tiramos o element '2' da fila, e contamos a partir do 2, dai retiramos
		 o elemento 4, e contamos a partir do 5, retiramos o elemento 1 (modulo p), partimos do 3
		 e por fim retiramos o 5
		'''
        s = (i+j-1)%p+1
    return s

def solRecursive(p, j):
    if(p == 1):
        return p
    else:
        return (solRecursive(p-1, j) + (j-1)) % p + 1
    


print(solIterative(5, 3))
print(solIterative(5, 3))

if __name__ == '__main__':
    pass