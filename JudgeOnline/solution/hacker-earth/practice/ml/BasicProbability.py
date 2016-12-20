'''
Created on 14 de dez de 2016

@author: christoffer

https://www.hackerearth.com/practice/machine-learning/prerequisites-of-machine-learning/basic-probability-models-and-rules/tutorial/
'''

'''
Eventos mutuamento exclusivos: Sao eventos que nao podem ocorrer ao mesmo tempo, como
o resultado de um lancamento de uma moeda ou um dado
P(a ou b) = P(a) + P(b) a consequencia eh que P(A e B) = 0
https://pt.wikipedia.org/wiki/Eventos_mutuamente_exclusivos
https://pt.wikipedia.org/wiki/Conjuntos_disjuntos


Eventos independentes: Seja A e B eventos, se a ocorrencia de A nao afeta B, esses
eventos sao ditos independentes
http://www.cpdee.ufmg.br/~rdmaia/EST_BAS/COMUM/independencia.pdf
http://www.portalaction.com.br/probabilidades/14-eventos-independentes-e-probabilidade-condicional

P(a e b) = P(a) * P(b)

Regra da soma
https://www.eecis.udel.edu/~portnoi/classroom/prob_estatistica/2005_2/lecture_slides/Aula07-Probabilidade-Regras-definicoes-adicao.pdf
http://www.mathgoodies.com/lessons/vol6/addition_rules.html
A palavra chave na regra da adicao eh o "ou"
Exemplo
QUal a chance de sair um numero impar num lancamento de dados
S = 6, Eventos favoraveis = 3
P(1) + P(3) + P(5) = 1/6 + 1/6 + 1/6 = 3/6

Quando falamos de eventos mutuamente exclusivos nao precisamos tomar cuidados adicionais, nos
casos que nao seguem essa regra (2 eventos nao mutuamente exclusivos),
quando um evento tem a chance de assumir 2 resultados, precisamos
remover da soma esses resultados, para evitar contagem duplicada. Exemplo

Numa sala com 100 pessoas, quais sao as chances de escolhermos uma pessoa com olhos verdes e cabelo
claro ?
A = pessoa com cabelo claro, B =ou pessoa com olho verde
S = numero total de pessoas no grupo
P(A ou B ) = P(A) + P(B) - P(A e B)


Marginal distribution eh o contraste de Conditional Distribution
https://en.wikipedia.org/wiki/Marginal_distribution
http://sites.nicholas.duke.edu/statsreview/probability/jmc/


'''
from sys import stdin, stdout

def fx(pbm, pam, pc):
    '''
        PA(chances de Mike pegar o onibus e Alice nao pegar
        PB(chances de Alice pegar o onibus e Mike nao pegar)
        PC(chance de chover)
        PC * (PA + PB)
    '''
    return pc * ( (pbm * (1 - pam) ) + (pam * (1 - pbm)) )

def read():
    return stdin.readline().strip()

def run():
    readFloat = lambda : float(read())
    pbm = readFloat()
    pam = readFloat()
    pc = readFloat()
    ans = fx(pbm, pam, pc)
    stdout.write( "{0:.6f}".format(ans) )

run()

#print(fx(0.2, 0.2, 0.5)) 

if __name__ == '__main__':
    pass