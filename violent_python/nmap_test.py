import nmap
import optparse

def nmapScan(tgtHost, tgtPort):
    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHost, tgtPort)
    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    print (" [*] " + tgtHost + " tcp/" + tgtPort + " " + state)

def main():
    parser = optparse.OptionParser('usage%prog ' + '-H <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify target ports')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = options.tgtPort
    #tgtPorts = str(options.tgtPort).split(' , ')
    #print(tgtPort)
    x = tgtPorts.split(',')
    print('ports:',x)
    print(type(x))

    #if (tgtHost == None) | (tgtPorts[0] == None):
     #   print(parser.usage)
      #  exit(0)
    for tgtPort in x:
        nmapScan(tgtHost, tgtPort)
    

if __name__ == '__main__':
    main()
