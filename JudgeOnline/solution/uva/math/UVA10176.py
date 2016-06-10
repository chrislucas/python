'''
Created on 10 de jun de 2016

@author: C.Lucas
https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1117
DONE
'''
from sys import stdin, stdout

MOD = 131071

def fromAnyToAny(number, _from, to):
    return None

def anyBaseToDec(number, base):
    #stdout.write("%s\n" % (number))
    acc = 0
    for num in number:
        acc *= base
        acc += int(num)
        acc = acc % MOD
    stdout.write("%s\n" % ( 'YES' if acc == 0 else 'NO' ))
    return acc

def solution():
    while True:
        try:
            line = stdin.readline().strip()
            if not line:
                break
            if(line.endswith('#')):
                line = line[:len(line)-1]
            else:
                while True:
                    #ch = stdin.read(1)
                    line2 = stdin.readline().strip()
                    '''
                    for ch in stdin.readline().strip():
                        if ch == '#':
                            break
                        if ch != '\n':
                            #line.append(ch)
                            line += ch
                    '''
                    line += line2
                    if(line.endswith('#')):
                        line = line[:len(line)-1]
                        break
            #line = ''.join(line)
            anyBaseToDec(line, 2)
        #except OSError as err:
        except EOFError:
            #print("Error: %s\n " % (err))
            break
solution()
if __name__ == '__main__':
    pass