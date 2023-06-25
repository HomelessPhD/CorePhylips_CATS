import hashlib
import bip39
import bip32

import buidl
from buidl.ecc import PrivateKey, Signature
from buidl.helper import decode_base58, big_endian_to_int
from buidl.bech32 import decode_bech32, encode_bech32_checksum
from buidl.script import P2PKHScriptPubKey, RedeemScript, WitnessScript, P2WPKHScriptPubKey
from buidl.tx import Tx, TxIn, TxOut
# https://bitcoinpy.dev/docs/bip-utils/



import codecs

# Define base58
def WIF(address_hex):
    PK0 = "841846de7afbe32ee7ded837872c6e0825db095275b8afed0000000000000000"
    PK1 = '80'+ PK0
    PK2 = hashlib.sha256(codecs.decode(PK1, 'hex'))
    PK3 = hashlib.sha256(PK2.digest())
    checksum = codecs.encode(PK3.digest(), 'hex')[0:8]
    PK4 = PK1 + str(checksum)[2:10]  #I know it looks wierd

    alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    b58_string = ''
    # Get the number of leading zeros
    leading_zeros = len(PK4) - len(PK4.lstrip('0'))
    # Convert hex to decimal
    address_int = int(PK4, 16)
    # Append digits to the start of string
    while address_int > 0:
        digit = address_int % 58
        digit_char = alphabet[digit]
        b58_string = digit_char + b58_string
        address_int //= 58
    # Add ‘1’ for each 2 leading zeros
    ones = leading_zeros // 2
    for one in range(ones):
        b58_string = '1' + b58_string
    return b58_string

def make_data_url(filename):
	fin = open(filename, 'rb')
	contents = fin.read()
	import base64
	data_url = base64.b64encode(contents)
	fin.close()
	return data_url
	
    # Load the image and produce 256 bit entropy
cats_file_name = 'cats_2.jpeg'
b64_s = make_data_url(cats_file_name);
b64_s_sh256_bytes = hashlib.sha256(b64_s).digest()
    # Use the 256bit entropy to create a mnemonic phrase
mnemonic = bip39.encode_bytes(b64_s_sh256_bytes)


count = 0
with open("pass_list.txt") as fp:
    while True:
        count += 1
        passphrase = fp.readline()
        if not passphrase:
            break
        if (count % 100) == 1:
            print('Now at '+str(count))
            
            # Add a passphrase (Optional, but recommended)
        passphrase = passphrase.rstrip('\n');

            # Use the mnemonic and passphrase to generate the seed
        seed = bip39.phrase_to_seed(mnemonic, passphrase);

            # Use the seed to generate a p2wpkh address
        root = bip32.BIP32.from_seed(seed);
        private_key = PrivateKey(secret=big_endian_to_int(root.get_privkey_from_path("m/84'/0'/0'/0/0")), network="signet");
        address = private_key.point.p2wpkh_address();

            # Check if address suit the task
        if(address == 'bc1qcyrndzgy036f6ax370g8zyvlw86ulawgt0246r'):
        #if(address == 'bc1q57euh23y3qs2f9d5mtwpax5lqecfvrdkqce82a'):
            with open('found.txt', 'a') as result:
                result.write(f'{passphrase}|{private_key.hex()}|{WIF(private_key.hex())}\n')



