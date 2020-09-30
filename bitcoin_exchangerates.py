import sys
import os
import time
import blockchain
from blockchain import exchangerates
ticker = exchangerates.get_ticker()
os.system("clear")
time.sleep(1)
print ("    ######### Author : Rahat Khan Tusar ##########")
time.sleep(2)
print (" ########## Github : https://github.com/r3k4t ##########")
print
time.sleep(3)
print("Bitcoin prices in various currencies:")
for k in ticker:
 print (k,ticker[k].p15min)
