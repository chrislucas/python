'''
Created on Mar 28, 2016

@author: christoffer
'''
'''
interesante http://www.geeksforgeeks.org/competitive-programming-conquering-a-given-problem/
'''
#https://www.hackerrank.com/contests/intro-to-statistics/challenges/basic-statistics-warmup-2

from sys import stdin, stdout
import math

def readAndSplit(fmt):
    return stdin.readline().split(fmt)

def readInt():
    return int(stdin.readline())

def writeString(_str):
    stdout.write(_str)

# http://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
def writeDouble(_str, fmt):
    stdout.write(fmt % float(str(_str)))

'''
def test():
    writeDouble("13.49999999999999999999", "%.2f\n")
    print(float("{0:.2f}\n".format(13.49999999999999999999)))
    print(round(13.49999999999999999999, 2))
''' 
     
def readFloatList(fmt):
    return [float(e) for e in stdin.readline().split(fmt)]

def mean(numbers):
    _sum = 0.0
    sz  = len(numbers)
    for e in numbers:
        _sum += e
    return _sum / sz

def median(numbers):
    sz = len(numbers) - 1
    numbers.sort()
    return numbers[sz / 2] if (sz + 1) % 2 == 1 else (numbers[ (sz + 1) / 2] + numbers[ (sz) / 2]) / 2 

def mode(numbers):
    numbers.sort()
    mapNumbers = {}
    maxValue = 0
    for e in numbers:
        if(mapNumbers.has_key(e)):
            mapNumbers[e] += 1
        else:
            mapNumbers[e] = 1
        if(mapNumbers[e] > maxValue):
            maxValue = mapNumbers[e]
            value = e
    return value
    
def standartDeviation(numbers, meanValue):
    s = 0.0
    for e in numbers:
        s += (e - meanValue) ** 2
    
    return math.sqrt(s / len(numbers))

#mode([10, 20, 23, 10, 5, 5, 6, 7, 5])



q = readInt()
numbers = readFloatList(" ")

meanVal = mean(numbers)
meadVal = median(numbers)
modeVal = mode(numbers)
stndVal = standartDeviation(numbers, meanVal)

stdout.write( "%.0f\n" if meanVal == int(meanVal) else "%.1f\n" % (meanVal))
stdout.write( "%.0f\n" if meadVal == int(meadVal) else "%.1f\n" % (meadVal))
stdout.write( "%.0f\n" if modeVal == int(modeVal) else "%.1f\n" % (modeVal))
stdout.write( "%.0f\n" if stndVal == int(stndVal) else "%.1f\n" % (stndVal))

if __name__ == '__main__':
    pass