'''
Created on Jan 13, 2016

@author: christoffer
'''

#https://brilliant.org/problems/some-strings-of-code/

def decode():
    count = 0
    sequence_1 = 'ThisIsAStringOfCode'
    sequence_2 = 'HereIsAStringInCode'
    
    for i in range(0,len(sequence_1)):
        if sequence_1[i] != sequence_2[i]:
            count = count + 1
    return count
    
#print(decode())

# substrings
# str[start_inclusive:end_exclusive]
# str[start_inclusive:end_exclusive:step]
#print("5424234"[3:5])
'''
print( "%s %s %s" % 
       (
         "abcdef"[1:-3]      # imprime de char[1] ateh o antepenultimo char(exclusive)
        ,"abcdefgh"[-3]      # imprime o antepenultimo char
        ,"abcdef"[:-3]       # imprime do char[0] ateh o antepenultimo char(exclusive) 
        )
)
'''
#note que ao usar [:-N] isso faz com que o python exclua os N ultimos caracteres
print("%s %s %s\n\n"  %
    (
         "abcdef"[2:-2]     # imprimir a partir do 2 caracter mais exclui os ultimos 2 caracteres
        ,"abcdef"[4:-1]     #
        ,"abcdef"[:-1]
    )
)

# note que ao usar [::-N] vc indica ao python que os intervalos serao decrescentes
# logo string[::-N] imprimi "string" de tras para frente seguindo os intervalos
print("%s\n%s\n%s\n%s\n%s\n%s\n%s\n" %
    (
        "abcdfeg"[0::]          # imprime a partir do primeiro char
        ,"abcdfeg"[0::2]        # idem, porem de 2 em 2
        ,"abcdfeg"[0:4:1]       # imprime entre [0 ... 2 (excluisve)] de 1 em 1
        ,"abcdfeg"[::-1]        # imprime de 1 em 1 de tras para frente
        ,"abcdfeg"[::-2]        # imprime 2 a 2 de tras para frente
        ,"abcdfeg"[:1:-1]       # imprime 1 a 1 ateh o caracter de indice 2, lembrando que em python [inclusive:excluive]
        ,"abcdfeg"[:0:-1]       # imprime de tras para frente terminando no primeiro caracter(exclusive)
    )
)

if __name__ == '__main__':
    pass