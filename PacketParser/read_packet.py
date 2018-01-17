#!/usr/bin/env python3

import sys
import pcap


def main(argv):
    print(pcap.findalldevs())
    read_interface = create_reading_interface()

    #while True:
    for index in range(0, 1):
        print(read_interface.stats(), read_interface.readpkts())
        #print(read_interface.readpkts())




def create_reading_interface():
    #read_interface = pcap.pcap(name = None, 
    read_interface = pcap.pcap(name = 'wlp4s0', 
                               promisc = False,
                               timeout_ms = 100)
    return read_interface





if __name__ == '__main__':
    sys.exit(main(sys.argv))
