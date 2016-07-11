'''
Created on 11 de jul de 2016

@author: C.Lucas
http://xael.org/pages/python-nmap-en.html
'''
import nmap

nm = nmap.PortScannerAsync()
nm.scan('127.0.0.1', '1111')

#print(nm.command_line())
for host in nm.all_hosts():
    print(host)

if __name__ == '__main__':
    pass