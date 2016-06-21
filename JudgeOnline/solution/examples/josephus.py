'''
Created on May 20, 2016

@author: christoffer
'''

'''
Procurar por solucao em O(kLogn) 
http://stackoverflow.com/questions/4845260/josephus-for-large-n-facebook-hacker-cup
http://www.geeksforgeeks.org/josephus-problem-set-1-a-on-solution/

Ler tambem
http://www.exploringbinary.com/powers-of-two-in-the-josephus-problem/
'''
def test(p, j):
    s = 1
    i = 1
    while i < p+1:
        s = (s + (j-1) ) % p + 1
        i+=1
    return s

def iterativeSol(p, k):
    person = 1
    for i in range(1, p+1):
        '''
         ans+k representa o salto partindo da ans-esima pessoa
         o -1 eh um 'ajuste', pois quando vc realiza um salto
         a partir da i-esima pessoa por exemplo i=1, um salto
         k = 3 deveria nos levar a terceira pessoa, mas i+3=4. Entao fazemos o ajuste
         No final da formula temos (modulo p + 1) o modulo p e para quando chegarmos
         ao fn]inal da fila circular, assim podemos recomeçar a contagem e o +1 eh um novo 'ajusto'
         Esse ajusta trata a retirada da i-esima pessoa da contagem. Lembrando, fizemos
         um salto k, retiramos o elemento i+k-1 da fila, agora temos que contar a partir do
         proximo elemento. Exemplo p = 5, k = 2
         no primeiro salto, tiramos o element '2' da fila, e contamos a partir do 2, dai retiramos
         o elemento 4, e contamos a partir do 5, retiramos o elemento 1 (modulo p), partimos do 3
         e por fim retiramos o 5
        '''
        person = (person + (k-1)) % i + 1
    return person

'''
https://en.wikipedia.org/wiki/Josephus_problem#k.3D2
Formula generalizada para qualquer K saltos
se f(1, k) = 1
entao f(n,k) = (f(n-1 , k) + (k-1)) % n + 1
se f(1, k) = 0
entao f(n, k) = (f(n-1, k) + k) % n
'''

def recursiveSol(p, k):
    if(p == 1):
        return p
    else:
        ans = recursiveSol(p-1, k)
        return  (ans + (k-1)) % p + 1
    


print(recursiveSol(5, 2))
print(iterativeSol(2, 3))

if __name__ == '__main__':
    pass