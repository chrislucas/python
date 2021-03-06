'''
Created on May 18, 2016

@author: christoffer
'''

'''
https://www.urionlinejudge.com.br/judge/pt/problems/view/1357
DONE
'''
from sys import stdin, stdout

class CompIO():
    def __init__(self):
        pass
    
    def getMapInt(self, fmt):
        return map(int, stdin.readline().splt(fmt))
    
    def readAndSplit(self, fmt):
        return stdin.readline().split(fmt)
    
    def readStringList(self, fmt):
        n = stdin.readline().rstrip("\n").split(fmt)
        return [e for e in n]
    
    def readInt(self):
        return int(stdin.readline())
    
    def readFloat(self):
        return float(stdin.readline())
    
    def readLine(self):
        return stdin.readline().rstrip("\n")
    
    # python nao suporta overload de metodos
    # mas suporta default values, como no parametro fmt
    # abaixo
    def writeString(self, _str, fmt = None):
        if(fmt is None):
            stdout.write(_str)
        else:
            stdout.write(fmt % str(_str))   
    
    def write(self, _str):
        stdout.write("%s" % str(_str))
    
    def writeArgs(self, fmt, *args):
        stdout.write(fmt % args)
    
    # http://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
    def writeDouble(self, _str, fmt):
        stdout.write(fmt % float(str(_str)))
        
    def readFloatList(self, fmt):
        return [float(e) for e in stdin.readline().split(fmt)]
    
    def readIntList(self, fmt):
        return [int(e) for e in stdin.readline().split(fmt)]

'''
def build_map_num_braille():
    braille = [
         ['.*', '**', '..']     # 0
        ,['*.', '..', '..']
        ,['*.', '*.', '..']
        ,['**', '..', '..']
        ,['**', '.*', '..']
        ,['*.', '.*', '..']
        ,['**', '*.', '..']
        ,['**', '**', '..']
        ,['*.', '**', '..']
        ,['.*', '*.', '..']
    ]
    _map = {0 : '', 1 : '', 2 : '', 3 : '', 4 : '', 5 : '', 6 : '', 7 : '', 8 : '', 9 : ''}
    for line in range(0, len(braille)):
        _map[line] = _map[line].join(braille[line]) 
    return _map
print(build_map_num_braille())       
''' 

#io.writeArgs("%d %d %d", 1, 2, 3)
#a, b, c = braille[0]
#io.writeArgs("%s\n%s\n%s", braille[0][0], braille[0][1], braille[0][2])

def print_braille(_list):
    braille = [
         ['.*', '**', '..']     # 0
        ,['*.', '..', '..']
        ,['*.', '*.', '..']
        ,['**', '..', '..']
        ,['**', '.*', '..']
        ,['*.', '.*', '..']
        ,['**', '*.', '..']
        ,['**', '**', '..']
        ,['*.', '**', '..']
        ,['.*', '*.', '..']
    ]
    i = 0
    while i < 3:
        for j in range(0, len(_list)):
            fmt = "%s" if j == 0 else " %s"
            io.writeString(braille[_list[j]][i], fmt)
        io.write("\n")
        i += 1
    #io.write("\n")
    # fim metodo

#print_braille([1,2,3,4,5,6,7,8,9,0])
#print_braille([0,0])

def print_numeros(_list = None):
    map_braille = {
         0:'.***..'     # 0
        ,1:'*.....'
        ,2:'*.*...'
        ,3:'**....'
        ,4:'**.*..'
        ,5:'*..*..'
        ,6:'***...'
        ,7:'****..'
        ,8:'*.**..'
        ,9:'.**...'
    }
    '''
    braille = [
         ['.*', '**', '..']     # 0
        ,['*.', '..', '..']
        ,['*.', '*.', '..']
        ,['**', '..', '..']
        ,['**', '.*', '..']
        ,['*.', '.*', '..']
        ,['**', '*.', '..']
        ,['**', '**', '..']
        ,['*.', '**', '..']
        ,['.*', '*.', '..']
    ]
    if(_list == None):
        _list = []
        for i in range(0, len(braille)):
            _list.append(map_braille[i])
    '''        
    
    for text in _list:
        #  As you are in python3 , use dict.items() instead of dict.iteritems()
        for k, v in map_braille.items():
            if(text == v):
                io.write(k)
                break
    io.write("\n")
    # fim metodo

io = CompIO() 
def solver():
    try:
        while True:
            x = io.readInt()
            if(x == 0):
                break
            
            if(io.readLine() == 'S'):
                _list = [int(e) for e in list(io.readLine())]
                print_braille(_list)
            
            else:
                _matrix = [''] * x
                i = 0
                while i < 3:
                    line = io.readStringList(' ')
                    for j in range(0, len(line)):
                        _matrix[j] += line[j] 
                    i+=1
                    
                print_numeros(_matrix)
             
    except IOError:
        pass

#http://stackoverflow.com/questions/10905423/how-to-compare-keyboard-input-to-a-string-in-python
#print(io.readLine() == 'S')
#print(io.readStringList(" "))

solver()

if __name__ == '__main__':
    pass