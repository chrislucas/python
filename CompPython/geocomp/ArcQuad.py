'''
Created on Apr 27, 2016

@author: christoffer
'''
import math
from math import ceil

'''
http://www.tutorbrasil.com.br/estudo_matematica_online/faq_matematica/4arcosnoquad.php
'''

def area(ladoQuad):
    # area do quadrado
    aTotal      = ladoQuad ** 2
    # area do triangulo (explicacao no link a cima)
    aTriangle   = ((ladoQuad ** 2) * (3 ** 0.5)) / 4
    
    # 1/6 da area do circulo, setor do lado direito do quadrado (na imagem esta pintado de verde agua)
    aSetor1     = (math.pi * (ladoQuad ** 2)) / 6
    # area do arco que forma a base do triangulo (ver o link acima, na imagem esta pintada de verde escuro)
    aArc1       = abs(aSetor1 - aTriangle) 
    
    # 1/12 avos da area do circulo, setor do lado inferior do quadrado
    aSetor2     = (math.pi * (ladoQuad ** 2)) / 12
    # area no quanto infeior do quadrado (ver no link acima, esta pintada de verde)
    area2       = abs(aSetor2 - aArc1)
    # 1/4 da circunferencia (ver no link, esta pintada com um amarelo estranjo)
    aSetor3     = (math.pi * (ladoQuad ** 2)) / 4
    # area de um dos setores que ficam nos cantos (os menores, ver na imagem)
    areaMenor  = abs(aTotal - aSetor3 - area2)
    
    # agora calcular a area das pontas do arco
    areaPontaArc = area2 - areaMenor
    
    # 4 vezes a area das pontas pois sao quatro pontas
    areaPontaArc = areaPontaArc * 4
    # 4 vezes a area do setorMenot pois sao quatro setores menores
    areaMenor   = areaMenor * 4
    '''
        Para obtermos a area do centro subtraimos da areaTotal os valores
        das areas dos setores menores e 
    '''
    areaCentro = aTotal - areaPontaArc - areaMenor
    C = 1000
    return [ ( (areaCentro * C + 0.5) / C, 2)
            ,( (areaPontaArc * C + 0.5) / C)
            ,( (areaMenor * C + 0.5) / C)
        ]

print(area(0.2))

if __name__ == '__main__':
    pass