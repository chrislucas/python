'''
Created on 21 de dez de 2016

@author: christoffer
'''

if __name__ == '__main__':
    pass

def modSum(a, b , m):
    return (a%m+b%m)%m

def binomialTable(n, p, m):
    table = [ [0] * (p+1) for i in range(n+1)]
    for i in range(0, n+1):
        for j in range(0, min(i, p)+1):
            table[i][j] = 1 if(j == 0 or j == i) else modSum(table[i-1][j-1] , table[i-1][j], m ) #table[i-1][j-1] + table[i-1][j]
    return table

def binomialList(n, p, m):
    table = [0] * (p+1)
    table[0] = 1
    for i in range(1, (n+1)):
        for j in range(min(i, p), 0, -1):
            table[j] = table[j] + table[j-1]
    return table

def binomialFormulaRec(n, p, m):
    if(p == 0 or n == p):
        return 1
    x = binomialFormulaRec(n-1, p-1, m)
    y = binomialFormulaRec(n-1, p, m)
    return modSum(x, y, m) # x + y

table = binomialList(5, 2, 100000)
#table = binomialTable(20, 12, 1000000)
#print(table[20][12])

# print(binomialFormulaRec(20, 12, 1000000))

