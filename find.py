import os,sys

import util

filename=sys.argv[1]
#print(filename)
file=open(filename,"r")

msg=util.find_secret_message(file)
print(msg)