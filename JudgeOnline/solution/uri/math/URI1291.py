'''
Created on Apr 27, 2016

@author: christoffer
'''
from sys import stdin, stdout
import math

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
    return [ ( (areaCentro * C) / C), ( (areaPontaArc * C) / C), ( (areaMenor * C) / C)]    
    #return [areaCentro, areaPontaArc, areaMenor]
    
class CompIO():
    
    def __init__(self):
        pass
    
    def readAndSplit(self, fmt):
        return stdin.readline().split(fmt)

    def readInt(self):
        return int(stdin.readline())
    
    def readFloat(self):
        return float(stdin.readline())
    
    def writeString(self, _str):
        stdout.write(_str)
    
    # http://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
    def writeDouble(self, _str, fmt):
        stdout.write(fmt % float(str(_str)))
        
    def readFloatList(self, fmt):
        return [float(e) for e in stdin.readline().split(fmt)]
def s():
    while True:
        try:
            io = CompIO()
            n = io.readFloat()
            rs = area(n)
            '''
            a = round(rs[0], 3)
            b = round(rs[1], 3)
            c = round(rs[2], 3)
            stdout.write( "%.3f %.3f %.3f\n" % (a, b, c) )
            '''
            # essa solucao eh mais rapida no URI
            stdout.write( "%.3f %.3f %.3f\n" % (rs[0], rs[1], rs[2]) )
        except:
            break
        
s()
    
if __name__ == '__main__':
    pass