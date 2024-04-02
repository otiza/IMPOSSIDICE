import random
import blocksmith
import sys
import json
import requests
#import postgresql client
import psycopg2
psqlurl = "postgresql://onlytiza2001:gSxZO62zJViM@ep-bitter-mouse-a2imk5dm.eu-central-1.aws.neon.tech/db-adminjs?sslmode=require"
conn = psycopg2.connect(
     host="ep-bitter-mouse-a2imk5dm.eu-central-1.aws.neon.tech",
        database="db-adminjs",
        user="onlytiza2001",
        password="gSxZO62zJViM",
        sslmode="require",
        port="5432"
)
cur = conn.cursor()
## if found balance, save to database

def hola(num):

    api_key = "F92Z14GE2DTF6PBBYY1YPHPJ438PT3P2VI"
    url = "https://api.etherscan.io/api?module=account&action=balancemulti&apikey=F92Z14GE2DTF6PBBYY1YPHPJ438PT3P2VI&address="
    keysperpage = 128
    totalpages= 904625697166532776746648320380374280100293470930272690489102837043110636675
    keys = {}
    pagenumber= int(num)
    basepage = pagenumber-1
    firstseed= basepage*keysperpage
    for j in range(firstseed,firstseed+keysperpage-1):
        privatekey = '{:064x}'.format(j+1)
        publickey = str(blocksmith.EthereumWallet.generate_address(privatekey))
        keys[publickey]=privatekey


    for i in range(0,keysperpage,20):

            addresses = list(keys.keys())[i:i+20]
            urls= url + ",".join(addresses)
            response = requests.get(urls)
            data = json.loads(response.text)
            
            for k in data['result']:
                try:
                    if int(k['balance'])>0:
                        ## save to database
                        cur.execute("INSERT INTO result (wallet,key,balance) VALUES (%s,%s,%s)",(k['account'],keys[k['account']],k['balance']))
                        conn.commit()

                        print("Public key: "+k['account']+" Private key: "+keys[k['account']] + " Balance: "+k['balance'])
                        with open("keys.txt", "a") as myfile:
                            myfile.write("Public key: "+k['account']+" Private key: "+keys[k['account']] + " Balance: "+k['balance']+"\n")
                except :
                    with open("keys.txt", "a") as myfile:
                           
                            myfile.write("result"+str(data['result'])+"\n")
                            myfile.write("keys"+str(keys)+"\n")

hola(sys.argv[1])

# while(1):
#      rand = random.randint(1,904625697166532776746648320380374280100293470930272690489102837043110636675)
#      hola(rand)