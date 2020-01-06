
text = '''
------------------------------------------------------------------------------------------------
This is not meant to be an aid to explain how to use OfflinePaperWallet, but rather
to explain how this application works under the hood. All the source code and 
explanations showing how this application was packaged is available on github at
https://github.com/andreshyer/OfflinePaperWallet.
------------------------------------------------------------------------------------------------

General Information:
All the private key and public address that generated in application are 
generated using python built-in packages as well as the external packages: 
ecdsa, base58, and Crypto. Also this application is completely self-contained. 
Meaning the machine never has to be connected to the internet for this 
application to work. 

How private keys are generated:
This is the most critical aspect of generating wallets. A wallet is only
as secure as the private key backing it. All the private keys for Bitcoin, 
Ethereum, and Litecoin are all generated the same way using the SHA256 
hashing protocol. What the SHA256 protocol does is it takes a string that the 
user inputs, it can be any string, and converts that into a 256-bit int. The 
exact details on how the SHA256 protocol works I will not explain here, but the 
way the SHA245 hashing protocol was implemented was by using the python built-in 
package hashlib. When the user inputs a passphrase into the terminal, all that 
is happening to generate the private is the passphrase is pass through the SHA256 
protocol, and the output is the private key.
!!!!!DO NOT REUSE PRIVATE KEYS FOR ANY REASON WHATSOEVER!!!!!
Even though in theory you could reuse private keys, don't for your and everyone 
else's safety.

Non-recoverable Mode:
When generating a new address, the option for 'non-recoverable' is available. 
By default, the private keys generated are recoverable by the passphrase provided 
by the user. The reason for this is that the passphrase the user provides is 
converted into a private key by the hash SHA256 protocol. When non-recoverable mode 
is activated, two additional pieces of information are feed into the string that 
can not be reproduced. One is a number that is randomly generated between 1 and 
10^100, and the other is the exact time the private key was generated. The random 
number is generated by the python built in package, secrets. Secrets is a 
cryptography grade package that specializes in, well, cryptography. One aspect of
cryptography is random number generation. Also, the time is extracted using the python 
built in package time. When time is return, a string is produced that is then converted 
into an int. For example, if the private key was generated 2019-1-4 10:45.4561, the 
int returned is 20191410454561. So the new string that is feed into the SHA256 protocol is 
[string given by user + time private key was created + random number between 1 and 10*100]. 
Since the random number nor the exact time and date can not be reproduced, that makes the 
private key generated non-recoverable. 

Mnemonic Seed, electrum based:
An mnemonic seed is a way to encode a private key in a user friendly fashion. 
So instead of writing down a private key where the user could easily mis-write 
a letter or number, the user can write down a mnemonic which can be decoded as 
a private key. So in other words, a mnemonic seed is just a representation of 
the private key. The protocol to generate a mnemonic seed is. 

private key > mnemonic encode > mnemonic seed (24 words)
mnemonic seed (24 words) > append checksum > mnemonic seed (25 words)

Private key to public address:
This section will attempt to briefly explain the idea of how the public addresses are 
generated, in this script. Bitcoin (BTC) and Litecoin (LTC) follow extremely, 
similar protocols to generate public addresses. This is  because LTC is a hard fork 
from BTC. BTC and LTC addresses are formed in the major steps:

private key > SECP256k1 elliptic curve > add extension b"04" > public key |
public key > SHA256 > add extension 2 > hashed public key |
hashed public key > SHA256 > SHA256 > checksum |
BTC/LTC address = hashed public key + checksum

The only difference between LTC and BTC addresses are that extension 2 for 
BTC = b"00" and for LTC = b"30".
If you want to see the theory behind this, please refer to 
https://www.freecodecamp.org/news/how-to-create-a-bitcoin
-wallet-address-from-a-private-key-eca3ddd9c05f/
in the blog they give very detailed instruction on the theory behind 
private > address. I did not use his code because I found his code to be 
rather clunky, but it is still useful to understand.

The process to make a ethereum (ETH) address is much simpler than that of 
BTC/LTC. The idea is basically the same, however, run private key through 
some elliptic curve and hash the result. The major steps to form a ETH 
wallet are:

private key > SECP256k1 elliptic curve > public key |
public key > keccak > last 20 bytes from hash > add extension "0x" > ETH address

Monero is the most complicated wallet to generate from the wallets in this
application. There are multiple protocols to generate a monero wallet.
The most popular, and the protocol used in this application, is to generate the
keys from a electrum based mnemonic seed. 

private key > sc_reduce32 > private spend key
private spend key > keccak_256 > sc_reduce32 > private view key

private view key > ed25519 > public view key
private spend key > ed25519 > public spend key

public address data = b"18" + public spend key + public view key
public address > keccak_256 > checksum
public address data = public address + first four byte of checksum

The string is converted to Base58. It is not done 
all at once like a Bitcoin address, but in 8-byte blocks. This gives us 
eight full-sized blocks and one 5-byte block that are appended together, 
to generate the full public address

public address data > base58 chunk coding > public address

I found this protocol from Cryptonote's website, but an easy to digest place to 
test the protocol can be found here https://xmr.llcoins.net/addresstests.html. 

To implement these protocols into python, I used the package ecdsa for the 
SECP256k1 curve, Crypto for the keccak curve, and hashlib for the SHA256 hashing 
algorithm. Also binascii was used to decode and encode hex formatted numbers
If you wish to see the code for how this was done, please refer to 
https://github.com/andreshyer/OfflinePaperWallet

Additional Notes
While this tool is 'safe', it is obvious that you should trust no one, especially 
when crypto-currency is involved. I would personally recommend testing a few keys 
that you do not intend to use on the different blockchains to make sure that they 
work fine. It is strongly encourage for you too look through the source code and 
make sure they are no obviously buggy/malicious code. The code is /fairly/ simple, 
anyone can look and see there are no online sources being used and that I am not 
just sending information to myself or anyone else, or just randomly choosing private
keys from a list of private keys.

Upcoming developments
These are changes that I would like to add in the near future.
1) Mnemonic Seed for Ethereum
2) Option for more cryto-currencies (Suggestions welcomed!)
3) Support for Linux/Mac (Mainly Linux, I do not own a Mac)
4) Better Help Screen(s)

Where can I donate?
You can't.
I did not make this for profit, I made this for my own needs. Since I needed a 
tool like this, figured others would like it as well. I got tried of having to 
make secure paper wallets. Boot up a live OS, go to a site, go offline, generate 
wallet, shutdown computer without going back online. That is a lot of work, I 
wanted something simple and secure. Also, I learned a lot about how wallets are 
generated form making this, which is more than enough for me.
'''

def print_help():
    print(text)

def return_help():
    return text