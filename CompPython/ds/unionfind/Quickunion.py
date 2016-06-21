'''
Created on Jun 3, 2016

@author: christoffer
'''

'''
Em quickuinion
id[idx] e o NO paid de idx
id[] = [0, 1, 9, 4, 9, 6, 6, 7, 8, 9]

NO pai de 2 eh o 9
id[2] = 9 e id[9] = 9
 O NO pai de idx eh encontrado da seguinte forma
 
id[ id[ id[ id[idx] ] ] ] -> uma busca em profundidade ate q idx == id[idx]

para saber se P e Q tem o mesmo no pai, basta veriticar se
pai(p) == pai(q)

A uniao de P e Q eh feita da seguinte forma'

defina a raiz de P com o valor da Raiz de Q
raizP = pai(P)
rauzQ = pai(Q)
id[raizP] = raizQ

'''

class Quickunion:
    '''
    classdocs
    '''
    id = []
    def __init__(self, n):
        '''
        Constructor
        '''
        self.id = [x for x in range(0, n)]
        None
    
    def root(self, idx):
        while idx != self.id[idx]:
            idx = self.id[idx]
        return idx
    
    def isConnected(self, p, q):
        rp = root(p) 
        rq = root(q)
        return rp == rq
    
    def union(self, p, q):
        rp = root(p)
        rq = root(q)
        self.id[rp] = rq
        
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
        root(self, idx)
    
    def union(self, p, q):
        rootP = root(p)
        rootQ = root(q)
        if rootP == rootQ:
            return None
        # se o n P tem mais nos associados a ele do que NO Q
        elif(he[rootP] > he[rootQ]):
            id[rootQ] = rootP           # o NO Q tera sua raiz modificada para raiz de P
            he[rootP] += he[rootQ]      # o pesso da raiz Q eh adicionado a raiz P
        
        else:
            id[rootP] = rootQ
            he[rootQ] += he[rootP]
    
    def isConnected(self, p, q):
        rp = root(p) 
        rq = root(q)
        return rp == rq
    
    def infoData(self):
        print(id)

def runTestWeightUF():
    ufw = WeightQuickUnion(10)
    ufw.union(1, 2)
    ufw.union(0, 1)
    ufw.infoData()
    
runTestWeightUF()



if __name__ == '__main__':
    pass