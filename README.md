<h2>Bitcoin_Exchangerates</h2>

<h4>Author : RKT</h4>

### Descripton ###


![a5c8348177c691359059d6eefa7ed964](https://user-images.githubusercontent.com/69615463/94634800-aa71f880-02ee-11eb-8e07-e3836b68d51b.gif)


### Getting bitcoin exchange rates from Blockchain.info ###

To install the Pi Blockchain tools library,open the command-line program and execute the following command:
<br>
<ul>
<li>python3 -m pip install --upgrade pip</li>
<li>sudo pip install blockchain</li>
</ul>
<br>

### The follwing steps shows the method for bitcoin exchange rates.First,import the exchangerates classes from the blockchain library : ###
#!/usr/bin/python3
<br>
#import blockchain
<br>
from blockchain import exchangerates
<br>

Exchange rates define a get_ticker method,which returns the exchange rates data in a dictionary object.Call this method and save the resulting object.The ticker dictionary object that we have has currency symbols as keys :</li></ul>
<br>
#get the bitcoin rates in various  currencies
<br>
ticker = exchangerates.get_ticker()
<br>

By running over these keys,data about the various  rates can be pulled.For example,the latest bitcoin rates can be obtainted in each currency by getting the p15min minimum value : 
<br>
#print the bitcoin price for every currency
<br>
print("Bitcoin prices in various  currencies:")
<br>
 for k in ticker:
  <br>
   print (k,ticker[k].p15min)
<br>


The following the screentshot shows the list of currencies and the equivalent bitcoin rate for those currencies at that moment or from the last 15 mintues :
 <br>
   <ul>
   <li>sudo python3 bitcoin_exchangerates.py</li>
</ul>

![Screenshot at 2020-09-30 07-00-05](https://user-images.githubusercontent.com/69615463/94634840-cd9ca800-02ee-11eb-8ed5-f5aaaa784105.png)



