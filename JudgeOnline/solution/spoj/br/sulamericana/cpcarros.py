'''
Created on 25 de nov de 2016

@author: C.Lucas
'''

# http://br.spoj.com/problems/CPCARROS/
# https://www.urionlinejudge.com.br/judge/problems/view/1363



from sys import stdin


def iesimaPlaca(placa, ith):
    
    if ( placa['tipo'] == 'n'):
        return None
    
    return None

def processa(placa):
    '''
    Primeira placa velha AAA0000
    ultima placa velha ZZZ9999
    primeira do novo
    aaaaa00
    '''
    ans = {}
    if(placa[3].isdigit() and placa[4].isdigit()):
        ans['text' ] = placa[0:3]
        ans['numero'] = placa[3:7]
        ans['tipo'] = 'v'
        
    elif( not placa[3].isdigit() and not placa[4].isdigit() ):
        ans['text'] = placa[0:4]
        ans['numero'] = placa[5:7]
        ans['tipo'] = 'n'
    
    return ans

def run():
    while(True):
        strM, strI, conf = [x for x in stdin.readline().split(" ")]
        if(strM == '*' and strI =='*' and conf == '0'):
            break
        conf = int(conf)
        # https://docs.python.org/3/library/stdtypes.html#string-methods
        
        processa(strM)
        processa(strI)
        


    
run()

if __name__ == '__main__':
    pass