'''
Created on 30 de jun de 2016

@author: chrislucas

https://www.hackerrank.com/challenges/dip-image-segmentation-1
https://en.wikipedia.org/wiki/Pixel_connectivity#4-connected
http://homepages.inf.ed.ac.uk/rbf/HIPR2/connect.htm
https://www.cs.auckland.ac.nz/courses/compsci773s1c/lectures/ImageProcessing-html/topic3.htm
http://radio.feld.cvut.cz/matlab/toolbox/images/binary6.html
'''
from sys import stdout

'''
Pesquisar por
connected-component labeling algorithm
Usando UnionFind
https://en.wikipedia.org/wiki/Connected-component_labeling

http://stackoverflow.com/questions/22498375/finding-connected-components-in-an-image-using-python
http://stackoverflow.com/questions/22051069/how-do-i-find-the-connected-components-in-a-binary-image/22085423#22085423
http://www.scipy-lectures.org/packages/scikit-image/auto_examples/plot_labels.html
'''

ImageBin = [
     [0,0,0,1,1,0,0,0,1,0,1,0]
    ,[1,1,1,0,1,1,1,1,0,0,0,1]
    ,[1,1,1,0,1,0,0,1,0,0,1,0]
    ,[1,0,0,0,0,0,0,0,0,1,0,0]
]


def process(Image):
    '''
    for lin in range(len(Image)):
        for col in range(len(Image[lin])):
            stdout.write("%d" %(Image[lin][col]))
        stdout.write("\n")
    '''
    count = 0
    limitI = len(Image)
    for i in range(0, limitI):
        limitJ = len(Image[i])
        for j in range(0, limitJ):
            if(Image[i][j] == 1):
                #if(Image[i][j-1] == 1 and Image[i][j+1] == 1 and Image[i+1][j] == 1 and Image[i-1][j] == 1):
                if(i+1 < limitI and Image[i+1][j] == 1):
                    count += 1
                elif(i-1 > 0 and Image[i-1][j] == 1):
                    count += 1
                elif(j-1 > 0 and Image[i][j-1] == 1):
                    count += 1
                elif(j+1 < limitJ and Image[i][j+1] == 1):
                    count += 1
    return count

'''
Usando uma dfs
http://stackoverflow.com/questions/22051069/how-do-i-find-the-connected-components-in-a-binary-image/22085423#22085423
'''

def dfs(mat, visited, x, y, set):
    visited[x][y] = set
    
    return None

def run(mat):
    '''
    Inicializando uma matriz 2D
    http://stackoverflow.com/questions/2397141/how-to-initialize-a-two-dimensional-array-in-python
    '''
    # Meio Jeito
    #visited = [[False]*len(mat[0])]*len(mat)
    # Jeito que eu vi
    visited = [ x[:] for x in [[0]*len(mat[0])]*len(mat) ]
    set = 1
    for lin in range(len(mat)):
        for col in range(len(mat[i])):
            if(mat[lin][col] == 1 and visited[lin][col] == 0):
                dfs(mat, visited, lin, col, set)
                set+=1
    return
run(ImageBin)

stdout.write("%d" % (process(ImageBin)))


if __name__ == '__main__':
    pass