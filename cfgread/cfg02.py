#!/usr/bin/env python3
######## EXPLORE READ ##########
## create file object in "r"ead mode
configfile = open("vlanconfig.cfg", "r")
print(configfile)

configfile1 = configfile.read()

configfile1list = configfile1.splitlines()
print(type(configfile1list))
#print(configfile1list)
print(configfile1list[-3])
configfile.close()
