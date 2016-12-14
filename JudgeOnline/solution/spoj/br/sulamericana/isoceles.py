'''
Created on 25 de nov de 2016

@author: C.Lucas
'''

'''
http://br.spoj.com/problems/ISOSCELE/
https://www.urionlinejudge.com.br/judge/problems/view/1378
https://icpcarchive.ecs.baylor.edu/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=2481
https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3346

https://lyfat.wordpress.com/2012/05/22/euclidean-vs-chebyshev-vs-manhattan-distance/
http://math.stackexchange.com/questions/139600/euclidean-manhattan-distance
https://xlinux.nist.gov/dads/HTML/euclidndstnc.html
https://xlinux.nist.gov/dads/HTML/manhattanDistance.html

https://www.codechef.com/problems/MDIST

'''

if __name__ == '__main__':
    pass

from sys import stdin
from math import sqrt

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def euclidianDistance(self, pb):
        diffX = abs(pb.x - self.x)
        diffY = abs(pb.y - self.y)
        return int(sqrt(diffX*diffX + diffY*diffY))
    
    def manhattanDistance(self, pb):
        diffX = abs(pb.x - self.x)
        diffY = abs(pb.y - self.y)
        return (diffX*diffX + diffY*diffY)
# http://brasilescola.uol.com.br/matematica/triangulo.htm
def isTriangle(a, b, c):
    if( (a + b > c and abs(a - b) < c) 
        and (b + c > a and abs(b - c) < a)
        and (a + c > b and abs(a - c) < b)):
        if (a != b and a != c and b == c 
            or (b != a and b != c and a == c)
            or (c != a and b != c and a == b) ):
            return 1    # isoceles
        elif(a == b and b == c):
            return 2    # equilatero
        else:
            return 3    # escaleno
    else:
        return -1


def read():
    return stdin.readline().rstrip("\n")


def s1(setPoints = []):
    cnt = 0
    for i in range(0, len(setPoints)-2):
        pa = setPoints[i]
        for j in range(i+1, len(setPoints)-1):
            pb = setPoints[j]
            for k in range(j+1, len(setPoints)):
                pc = setPoints[k]
                ab = pa.distance(pb)
                bc = pb.distance(pc)
                ac = pa.distance(pc)
                T = isTriangle(ab, bc, ac)
                if(T == 1):
                    cnt+=1
    print(cnt)

def s2(setPoints = []):    
    return None

def run():    
    while(True):
        points = int(read())
        if(points == 0):
            break
        setPoints = []
        while(points>0):
            x, y = [int(data) for data in read().split(" ")]
            point = Point(x, y)
            setPoints.append(point)
            points -= 1
        s1(setPoints)
run()
        
    