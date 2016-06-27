'''
Created on 20 de jun de 2016

@author: chrislucas
'''

class WeightUnionFind(object):
    '''
    classdocs
    '''
    def __init__(self, params):
        '''
        Constructor
        '''

'''
Weight Quick Union tem uma estragegia diferente na funcao
union. Para evitar que um no pai fique com muitos no filhos
uma lista de pesos eh utilizada, onde cada NO pai tem o numero
de NOS filhos associado a si. Dessa forma, realizar a operacao
UNION, antes eh feito um teste, de qual NO tem o menor numero
de NOS FILHOS associados. O no com menor numero de filhos torna-se
um NO filho tambem

Exemplo

P = root(p)
Q = root(q)
if size{P} > size{Q}
    id[Q] = P            # a rais de Q eh modificada para raz
    he[P] += he[Q]        # adiciona o numero de NOS associados a Q a P
else
    id[P] = Q            # raiz de P torna-se Q
    he[Q] += he[P]        # nos associaos a P sao samados em Q
'''
class WeightQuickUnion:
    id = []
    he = []
    
    def __init__(self, n):
        self.id = [x for x in range(0, n)]
        self.he = [1] * n
        None
    
    def root(self, idx):
        if idx == self.id[idx]:
            return idx
        return self.root(self.id[idx])
    
    def union(self, p, q):
        rootP = self.root(p)
        rootQ = self.root(q)
        if rootP == rootQ:
            return None
        # se o n P tem mais nos associados a ele do que NO Q
        elif(self.he[rootP] > self.he[rootQ]):
            self.id[rootQ] = rootP           # o NO Q tera sua raiz modificada para raiz de P
            self.he[rootP] += self.he[rootQ]      # o pesso da raiz Q eh adicionado a raiz P
        
        else:
            self.id[rootP] = rootQ
            self.he[rootQ] += self.he[rootP]
    
    def isConnected(self, p, q):
        rp = self.root(p) 
        rq = self.root(q)
        return rp == rq
    
    def infoData(self):
        print([x for x in self.id])

def runTestWeightUF():
    ufw = WeightQuickUnion(10)
    ufw.union(1, 2)
    ufw.union(0, 1)
    ufw.union(3, 2)
    ufw.infoData()
    
runTestWeightUF()

if __name__ == '__main__':
    pass      