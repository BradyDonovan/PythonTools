#!/usr/bin/env python3

import os
import sys

if len(sys.argv) == 1:
        print ("No arguments specified.")

else:
        targetIP = sys.argv[1]
        print "Target: "+targetIP
        yn = input("Run full nmap scan on "+targetIP+"? Enter Y/N to continue: ")
        if (yn == "yes" or yn == "y" or yn == "Y"):
                print ("Running full scan on "+targetIP)
                os.system('nmap -Pn -n -v -sT --host-timeout=30m -p- '+targetIP+' -oA '+targetIP+'_allports')
        if (yn == "no" or yn == "n" or yn == "N"):
                print ("Scan cancelled. Quitting.")
