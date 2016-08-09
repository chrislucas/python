'''
Created on 11 de jul de 2016

@author: C.Lucas
http://xael.org/pages/python-nmap-en.html
'''
import nmap
import optparse

print(nmap.__path__[0])
#nn = nmap.PortScanner(nmap.__path__[0])


def main():
    params = 'usage%prog'+\
    '-H <target host> -p <target port>'
    _parse = optparse.OptionParser(params)
    _parse.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    _parse.add_option('-p', dest='tgtPort', type='string', help='specify target port[s] separate by comma')
    _options, args = _parse.parse_args()
    tgtHost = _options.tgtHost
    tgtPort = str(_options.tgtPort).split(', ')
    
    if(tgtHost == None or tgtPort[0] == None):
        print(_parse.usage)
        return None
    
    for p in tgtPort:
        print(p)
    
main()

#nm = nmap.PortScannerAsync()
#nm.scan('127.0.0.1', '1111')

#print(nm.command_line())
'''
for host in nm.all_hosts():
    print(host)
'''

if __name__ == '__main__':
    pass