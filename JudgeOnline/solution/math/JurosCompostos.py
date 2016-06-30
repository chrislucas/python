'''
Created on 28 de jun de 2016

@author: chrislucas

http://brasilescola.uol.com.br/matematica/juros-compostos.htm
http://www.somatematica.com.br/emedio/finan3.php
http://fazaconta.com/juros-compostos.htm
'''
from sys import stdout

'''
M = C * (1 + TAXA) ^ TEMPO
M / (1 + TAXA) ^ TEMPO = C
'''

def juros_comp(capital, taxa,  n):
    montante = capital * ((1 + taxa) ** n)
    return montante

# JUROS = Montante - Principal
def juros(capital, taxa,  n):
    return capital * ((1 + taxa) ** n) - capital

'''
  Calcule o montante de um capital de R$6.000,00,
  aplicado a juros compostos, durante 1 ano, a taxa de 3,5% ao mes.
'''

stdout.write("%f %f\n%f\n" % (
     juros_comp(6000.0, 3.5/100, 12)
    ,juros(6000.0, 3.5/100, 12)
    ,juros_comp(7000.0, 1.5/100, 12)
    )
)


'''
Calcule o valor do capital que, aplicado a uma taxa de 2% ao mes,
rendeu em 10 meses a quantia de R$ 15.237,43?
'''
stdout.write("%f\n" % (15237.43 / ((1 + 2/100) ** 10) ))

'''
Qual a taxa de juros empregada sobre o capital de 
R$ 8.000,00 durante 12 meses que gerou o montante de R$ 10.145,93?
'''

'''
http://brasilescola.uol.com.br/matematica/juros-compostos.htm
M = C * (1 + TAXA) ^ TEMPO
M / C = (1 + X) ^ 12
D = (1 + X) ^ 12
D ^ (1/12) = (1 + X)
D ^ (1/12) - 1 = X
'''
stdout.write("%f\n" % ( ( ( 10145.93 / 8000 ) ** ( 1/12 ) ) -1 ) )



if __name__ == '__main__':
    pass