'''
Created on Sep 17, 2015

@author: christoffer
'''

while True:
    try:
        from sys import stdin, stdout
        n = stdin.readline()
        n = int(n)
        stdout.write("NO\n" if n % 2 > 0 or n < 3 else "YES\n")
    except:
        break
if __name__ == '__main__':
    pass