'''
Created on May 25, 2016

@author: christoffer


https://www.urionlinejudge.com.br/judge/pt/problems/view/1031

Problema indicado
http://www.spoj.com/problems/ANARC08H/

'''
'''
http://www.geeksforgeeks.org/josephus-problem-set-1-a-on-solution/
https://en.wikipedia.org/wiki/Josephus_problem
'''

# uma abordagem que chamo de bottom-up
# partindo do principui que temos uma permutacao com 1 elemento
# ate n elementos no problema de josephus
def josephusPermutation(n, k):
    p = 0
    # i<= n
    # k-1 para ajustar o salto
    # poe exemplo, comecando do elemento 1
    # dando um salto k, vou parar no elemento
    # k + 1, mas nao eh isso que queremos. Queremos
    # cair no elemento k, entao fazermos i + k -1
    # o valor de + 1 no final da formula, faz o ajuste
    # apos o salto. Assim que eliminamos o valor k da permutacao
    # comecamos a contagem a partir do elemento k+1
    for i in range(1, n+1):
        p = (i + (k-1)) % i + 1
    return p

print(josephusPermutation(14,2))

if __name__ == '__main__':
    pass