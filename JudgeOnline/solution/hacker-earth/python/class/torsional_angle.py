'''
Created on 9 de jul de 2016

@author: C.Lucas
https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle?h_r=next-challenge&h_v=legacy

http://www.mathsisfun.com/geometry/dihedral-angles.html
http://www.mat.ufmg.br/gaal/aulas_online/at4_11.html
http://math.stackexchange.com/questions/47059/how-do-i-calculate-a-dihedral-angle-given-cartesian-coordinates

http://stackoverflow.com/questions/20305272/dihedral-torsion-angle-from-four-points-in-cartesian-coordinates-in-python
http://pd.chem.ucl.ac.uk/pdnn/refine2/torsion.htm
'''

from sys import stdin

class Point:
    
    #def __init__(self, x, y, z):
    #http://stackoverflow.com/questions/682504/what-is-a-clean-pythonic-way-to-have-multiple-constructors-in-python
    def __init__(self, *args, **kargs):
        self.x, self.y, self.z = args
        #self.y = y
        #self.z = z
        print("%s %s %s" % (self.x, self.y, self.z) )
        
def run():
    x, y, z = [int(x) for x in stdin.readline().split(" ")]
    pa = Point(x, y, z)
    x, y, z = [int(x) for x in stdin.readline().split(" ")]
    pb = Point(x, y, z)
    x, y, z = [int(x) for x in stdin.readline().split(" ")]
    pc = Point(x, y, z)
    x, y, z = [int(x) for x in stdin.readline().split(" ")]
    pd = Point(x, y, z)

run()

if __name__ == '__main__':
    pass