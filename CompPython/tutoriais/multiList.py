'''
Created on 19 de nov de 2016

@author: C.Lucas
'''

if __name__ == '__main__':
    pass

# http://stackoverflow.com/questions/6667201/how-to-define-two-dimensional-array-in-python



def getMatrix(w, h):
    #Matrix = [ [0 for i in range(w)] for j in range(h)]
    #Matrix = [ [i] * w for i in range(h)]
    #Matrix = [[0]*w]*h
    Matrix = [[]*w]*h
    return Matrix

w, h = 5, 5
#print(list(range(5)), sep=" ")
getMatrix(w, h)