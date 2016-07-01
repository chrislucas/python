'''
Created on 22 de jun de 2016

@author: chrislucas

https://ucoder.com.br/problems/1267/
https://ucoder.com.br/problems/?q=&contest_text=V+MARATONA+DE+PROGRAMA%C3%87%C3%83O+INTERFATECS+2016+1%C2%AA+Fase
https://ucoder.com.br/problems/?q=&contest_text=IV+MARATONA+DE+PROGRAMA%C3%87%C3%83O+INTERFATECs+2015
https://ucoder.com.br/problems/?q=&contest_text=Interfatecs+2014+1%C2%AA+fase
https://ucoder.com.br/problems/?q=&contest_text=Interfatecs+2014+2%C2%AA+fase
'''
from sys import stdin, stdout

def valor_percentual(months, receivePerHour, hourPerMonth, per):
    return months * receivePerHour * hourPerMonth * per

def valor_futuro(capital, tax, time):
    return capital * ((1 + tax) ** time)

def f_juros(v_futuro, capital):
    return v_futuro - capital


def runTest():
    '''
        M = C * ( (1 + TAX) ^ TIME)
        M = 17627.81
        TAX (17627.81/C) ^ (1/TIME) - 1
    '''
    c = valor_percentual(1, 120, 160, .3)
    #d = ((17627.81/c) ** (1/3))-1

    stdout.write("%f %f\n" % (c, valor_futuro(5000, 4/100, 5))  )

runTest()

def calc (months, receivePerHour, hourPerMonth):
    return months * receivePerHour * hourPerMonth

def run():
    data = [float(x) for x in stdin.readline().split(" ")]
    ePerHourBrazil      = data[0]
    ePerHourForeign     = data[1]
    workingHours        = data[2]
    DPB                 = data[3]
    DPE                 = data[4]
    CT                  = data[5]
    
    calcBr = calc(3, ePerHourBrazil, workingHours)
    calcBr = calcBr - (calcBr * (DPB)/100) 
    calcFg = calc(3, ePerHourForeign, workingHours)
    calcFg = calcFg - (calcFg * (DPE)/100) 
    tax = 1/100
    valBr = valor_futuro(calcBr, tax, 3)
    valFg = valor_futuro(calcFg, tax, 3)
    
    stdout.write("%.2f %.2f" % (valBr, valFg) )

'''
100.00 31.00 120.00 70.00 85.00 4.03
120.00 27.00 160.00 70.00 71.00 4.60
'''

#run()

if __name__ == '__main__':
    pass