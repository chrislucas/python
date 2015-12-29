'''
Created on 28 de dez de 2015

@author: C.Lucas
'''

s = 0
for x in range(100001, 200000, 2):
    s += x
m = 0
for x in range(1, 100000, 2):
    m += x
print(s/m)

if s/m < 4:
    print (s/m)
else:
    print ('qualquer coisa')    

#strmsg = '1' if s/m < 4 else '0'
print ('1' if s/m < 4 else '0') #(strmsg)

if __name__ == '__main__':
    pass