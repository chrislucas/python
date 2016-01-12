'''
Created on Jan 7, 2016

@author: christoffer
'''

# https://www.hackerrank.com/challenges/quicksort2

def swap(array, i, j):
    aux = array[i]
    array[i] = array[j]
    array[j] =  aux

'''
existem ao menos 4 formas de pegar o elemento pivo
no metodo de particao do array, o exemplo abaixo 
utiliza o ultimo elemento do vetor como pivo;
Pega-se o elemento pivo e coloca-o na posicao correta
do array, depois disso todos os elementos menores
que o pivo a sua esquerda e todos os elementos maiores
a sua direita
'''
def partition(array, lf, ri):
    pivot = array[ri]   # pivo
    i = lf              # indice do menor elemento
    j = 1
    while (j < ri):
    #for j in range(1, ri):
        # verifica se o elemento corrente eh menor que pivo
        # para posiciona-lo corretamente no vetor
        if(array[j] <= pivot):
            # trocar a posicao do j-esimo elemento pelo i-esimo
            swap(array, j, i)
            i+=1
        j += 1
    swap(array, i+1, ri)
    return i+1

# forma de passar uma lista como parametro
def quicksort(array, lf, ri):
    #if(lf >= ri):
        #return
    if(lf < ri):
        part = partition(array, lf, ri)
        quicksort(array, lf, part-1)
        quicksort(array, part+1, ri)


def main():
    from sys import stdin, stdout
    sz      = stdin.readline()
    array   = [int(i) for i in stdin.readline().strip().split()]
    quicksort(array, 0, int(sz) - 1)
    # array.__len__() - 1
    stdout.write(str(array))

if __name__ == '__main__':
    main()