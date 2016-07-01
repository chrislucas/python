'''
Created on 22 de jun de 2016

@author: chrislucas

https://ucoder.com.br/problems/1267/
https://ucoder.com.br/problems/?q=&contest_text=V+MARATONA+DE+PROGRAMA%C3%87%C3%83O+INTERFATECS+2016+1%C2%AA+Fase
https://ucoder.com.br/problems/?q=&contest_text=IV+MARATONA+DE+PROGRAMA%C3%87%C3%83O+INTERFATECs+2015
https://ucoder.com.br/problems/?q=&contest_text=Interfatecs+2014+1%C2%AA+fase
https://ucoder.com.br/problems/?q=&contest_text=Interfatecs+2014+2%C2%AA+fase

DONE
'''
from sys import stdin, stdout

def valor_percentual(months, receivePerHour, hourPerMonth, per):
    return months * receivePerHour * hourPerMonth * per

def calc (months, receivePerHour, hourPerMonth):
    return months * receivePerHour * hourPerMonth

def Test():
    R = valor_futuro(5760, 0.01, 3) + valor_futuro(5760, 0.01, 2) + valor_futuro(5760, 0.01, 1)
    print(R)

def valor_futuro(capital, tax, time):
    return capital * ((1 + tax) ** time)

def sol(val, tax):
    return valor_futuro(val, tax, 3) + valor_futuro(val, tax, 2) + valor_futuro(val, tax, 1)

def sol2(val, tax, time):
    _sum = 0.0
    for i in range(time, 0, -1):
        _sum += valor_futuro(val, tax, i)
    return _sum
        
def run():
    data = [float(x) for x in stdin.readline().split(" ")]
    ePerHourBrazil      = data[0]
    ePerHourForeign     = data[1]
    workingHours        = data[2]
    DPB                 = data[3]
    DPE                 = data[4]
    CT                  = data[5]
    
    calcBr = ePerHourBrazil * workingHours * ((100 - DPB) / 100)
    calcFg = ePerHourForeign * workingHours * ((100 - DPE) / 100)
    valBr = sol2(calcBr, 0.01, 3)
    valFg = sol2(calcFg, 0.01, 3)
    
    stdout.write("%.2fBR %.2fES" % (valBr, valFg * CT) )

'''
100.00 31.00 120.00 70.00 85.00 4.03
120.00 27.00 160.00 70.00 71.00 4.60
'''

#run()

if __name__ == '__main__':
    pass