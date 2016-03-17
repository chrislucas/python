#import sys

from sys import stdin, stdout

def reader():
    return stdin.readline()
    
def writer(data):
    stdout.write(str(data))
    return

# leitura rapida de strings
#_str  = reader()
#writer(_str)

# leitura rapida de inteiros
_int = int(reader())
writer(_int)




if __name__ == '__main__':
    pass