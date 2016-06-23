'''
Created on 23 de jun de 2016

@author: chrislucas
'''

'''
def solve(k):
    strA = '3'
    i = 1
    while i < k:
        counter = 1
        strB = ''
        for j in range(1, len(strA) - 1):
            if strA[j] == strA[j-1]:
                ch      = strA[j]
                counter += 1
            else:
                counter = 1
                strB = "{0}{1}{2}".format(counter, ch, strB)
        strA = strB
        i+=1
    return strA
'''


def runTest():
    #_list = [solve(x) for x in range(1, 5)]
    #print(_list)
    print(0x0f)
    
runTest()  

if __name__ == '__main__':
    pass