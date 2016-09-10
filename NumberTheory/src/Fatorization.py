'''
Created on 9 de set de 2016

@author: chrislucas
'''


'''
https://pt.wikipedia.org/wiki/Fatora%C3%A7%C3%A3o_de_inteiros

Representacoes de um Inteiro Positivo como Somas de Inteiros Positivos Consecutivos
http://elementosdeteixeira.blogspot.com.br/2013/07/117-representacoes-de-um-inteiro.html
'''

'''
Representacao de inteireos
http://www.ime.usp.br/~pf/algoritmos/aulas/int.html
'''

'''
Primos
http://ccse.uepa.br/downloads/material_2011/NUMEROS_PRIMOS.pdf
'''

'''
constatacao importante: Teorema funadmenta da aritmetica
https://pt.wikipedia.org/wiki/Teorema_fundamental_da_aritm%C3%A9tica

Pelo teorema fundamenta da aritmetica, cada numero inteiro tem somente
ua decomposicao em numeros primos

'''
from math import sqrt
from sys import stdout
#http://marathoncode.blogspot.com.br/2012/03/numeros-primos-ii.html
#http://www.btinternet.com/~se16/js/factor.htm

'''
 Por caso
 PI (sqrt(n)) aproximadamente  2sqrt(n) / ln n
'''
def fatorar(n):
    fatores = []
    i = 2
    l = sqrt(n) + 1
    while(n > 1 and i < l):
        # se i divide n -> i eh primo
        while(n%i==0):
            fatores.append(i)
            n //= i
        i+=1
    '''
        Pode ocorrer de i chegar ate o limite sqrt(n)
        e 'n' for primo
        Por exemplo se n = 22
        no primeiro loop 22 % 2 == 0
        n = 22 / 2 = 11
        11 -> primo
        Quando ocorre de n ser primo, o valor de i vai aumentar
        e nao teremos divisores para n
    '''
    if(n>1):
        fatores.append(n)
    return fatores

'''
Prova de que o algoritmo acima funciona
o vetor fatores [] so deve receber numeros primos,
porem, suponhamos que por absurdo a um numero F composto
dentro do vetor

Segundo o teorema fundamental da aritmetica, todo numero composto
pode ser expresso por fatores primos (p1 + p2 + p3 + ... + pn) < F
(todos os fatores menores que F)

Entao se tivermos algum numero composto formado por fatores primos
menores do que F, esses numeros ja estariam no vetor, F ja teria sido
divido por ele, logo F nao poderia estar no vetor

'''
def test(n):
    for x in fatorar(n):
        stdout.write("%d " % ( x ) )
    stdout.write("\n")
    
def fatorar2(n):
    fatores = {}
    lim = sqrt(n)+1
    num = 2
    while(n > 1 and num < lim):
        while(n%num==0):
            if num not in fatores:
                fatores[num] = 1
            else:
                fatores[num] += 1
            n //= num
        num += 1
    if(n > 1):
        if n not in fatores:
            fatores[n] = 1
        else:
            fatores[n] += 1
    return fatores

def test2(n):
    _dict = fatorar2(n)
    if(hasattr(_dict, '__iter__')):
        for k, v in _dict.items():
            stdout.write("{%d:%d}\n" % (k, v)) 

'''
http://crbonilha.com/pt/1-exercicios-aleatorios/#more-549
'''
def oddDiv(n):
    _dict = fatorar2(n)
    ans = 1
    if(hasattr(_dict, '__iter__')):
        #for v in _dict.values():
        #for k in _dict.keys():
        for k, v in _dict.items():
            if(k == 2):
                continue
            ans *= (v+1)
    return ans

print(oddDiv(12))
   
if __name__ == '__main__':
    pass