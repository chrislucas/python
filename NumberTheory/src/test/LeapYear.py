'''
Created on 22 de jun de 2016

@author: C.Lucas

Resolver
https://www.urionlinejudge.com.br/judge/pt/problems/view/1279

https://en.wikipedia.org/wiki/Leap_year
'''
from sys import stdout

'''
No calendario gregoriano, a maioria dos anos multiplos de 4 sao anos bissextos. A cada quatro
anos um dia eh acrescentado ao mes de fevereiro para compensar o fato de que o periodo de 365
dia eh mais curto do que 1 ano Tropical uma difereca de quase 6 horas por ano
'''

'''
Algoritmo

wiki
Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100,
but these centurial years are leap years if they are exactly divisible by 400.
For example, the years 1700, 1800, and 1900 are not leap years, but the year 2000 is.
'''

def isLeap(year):
    if( (year % 4 == 0 or year % 400 == 0) and (not (year % 100 == 0) or year % 400 == 0)  ):
        return True
    else:
        return False
    
def isLeapYear(year):
    if ( year % 4 > 0):
        return False
    elif( year % 100 > 0):
        return True
    elif( year % 400 > 0):
        return False
    else:
        return True
    
def runTest():
    lst = [1996, 1600, 1700, 1800, 1990, 2000, 2016, 2200]
    for year  in lst:
        stdout.write("%s %s\n" % ( isLeap(year), isLeapYear(year)))

runTest()

if __name__ == '__main__':
    pass