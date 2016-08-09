'''
Created on 17 de jul de 2016

@author: C.Lucas
'''

'''
http://marathoncode.blogspot.com.br/2012/03/combinatoria-basica.html
http://www.geeksforgeeks.org/segmented-sieve/
'''


'''
http://introcs.cs.princeton.edu/java/14array/PrimeSieve.java.html
 *                  n     Primes <= n
 *  ---------------------------------
 *                 10               4   
 *                100              25  
 *              1,000             168  
 *             10,000           1,229  
 *            100,000           9,592  
 *          1,000,000          78,498  
 *         10,000,000         664,579  
 *        100,000,000       5,761,455  
 *      1,000,000,000      50,847,534  
'''
class Primes:
    def __init__(self):
        return None
      
    def crive_erathotenes(self, n):
        self.ListBool   = []
        self.ListNums   = []
        self.ListBool   = [True] * (n+1)
        self.ListBool[0], self.ListBool[1] = [False, False]
        limit = n+1
        for x in range(2, limit):
            if(self.ListBool[x]):
                y = x*x
                self.ListNums.append(x)
                while y < limit:
                    self.ListBool[y] = False
                    y += x
class Atkin:
    
    def __init__(self):
        return None
    
    def process(self, n):
        self.ListNums = [2,3,5]
        self.NonPrime = [False] * n+1
        limit = n+1
        

def runTestI():
    p = Primes()  
    p.crive_erathotenes(1000000)
    print(len(p.ListNums))

if __name__ == '__main__':
    pass