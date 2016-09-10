'''
Created on 8 de set de 2016

@author: chrislucas
'''


#http://br.spoj.com/problems/SIMUL09/

from sys import stdin, stdout

def inv(lista, a, b):
    while(a < b):
        aux = lista[a]
        lista[a] = lista[b]
        lista[b] = aux
        a+=1
        b-=1
    return

def soma(lista, a, b):
    ans = 0
    while(a <= b):
        ans += lista[a]
        a+= 1
    return ans

def init(n):
    return [x for x in range(0, n+1)]

def run():
    palavras, instrucoes = [int(x) for x in stdin.readline().split(' ')]
    lista = init(palavras);
    answers = []
    counter = 0
    while(instrucoes > 0):
        instrucao, a, b = [x for x in stdin.readline().split(' ')]
        a = int(a)
        b = int(b)
        if(instrucao == 'I'):
            inv(lista, a, b)
        else:
            #stdout.write("%d\n" % ( soma(lista, a, b) ) )
            answers.append(soma(lista, a, b))
            counter += 1
        instrucoes -= 1
    
    for x in answers:
        stdout.write("%d\n" % ( x ))
    
run()



if __name__ == '__main__':
    pass