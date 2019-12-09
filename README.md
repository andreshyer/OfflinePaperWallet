## OfflinePaperWallet

A simple application/python script to allow users to easily generate private keys and public 
addresses for common crypto-currencies. The support currencies are Bitcoin, Ethereum, and Litecoin.

OfflinePaperWallet is not sponsored or owned by any developer of Bitcoin, Ethereum, or Litecoin. That means this is an
unofficial application, and should be validated by experienced users. I will provide information on how this
application works, and why it is safe to use. There are a few different offline tools that do serve a similar propose
to what this provides. The difference is that here I will try and explain how the private keys and public addresses are
being generated. Hopefully this can provide confidence that this is a safe tool to use.

## General Help

This is a terminal tool, meaning that commands must be typed. Typing in the number '3' will lead to option 3 being
executed. There is not much else to really explain.

## General Information

All the private key and public address that generated in application are generated using python built-in packages as
well as the external packages: ecdsa, base58, and pysha3. Also this application is completely self-contained. Meaning
the machine never has to be connected to the internet for this application to work. Also, all the source code for this
application is available at https://github.com/andreshyer/OfflinePaperWallet

## How private keys are generated

All the private keys for Bitcoin, Ethereum, and Litecoin are all generated the same way using the SHA256 hashing
protocol. What the SHA256 protocol does is it takes a string that the user inputs, it can be any string, and converts
that into a 256-bit int. The exact details on how the SHA256 protocol works I will not explain here, but the way the
SHA245 hashing protocol was implemented was by using the python built-in package hashlib. When the user inputs a
passphrase into the terminal, all that is happening to generate the private is the passphrase is pass through the
SHA256 protocol, and the output is the private key.
!!!!!DO NOT REUSE PRIVATE KEYS FOR ANY REASON WHATSOEVER!!!!!
Even though in theory you could reuse private keys, don't

## Non-recoverable Mode

When generating a new address, the option for 'non-recoverable' is available. By default, the private keys
generated are recoverable by the passphrase provided by the user. The reason for this is that the passphrase the user
provides is converted into a private key by the hash SHA256 protocol. When non-recoverable mode is activated, two 
additional pieces of information are feed into the string that can not be reproduced. One is a number that is randomly
generated between 1 and 10^100, and the other is the exact time the private key was generated. The random number is
generated by the python built in package, secrets. Secrets is a cryptography grade package that specializes in, well,
cryptography. One aspect of cryptography is random number generation. Also, the time is extracted using the python built
in package time. When time is return, a string is produced that is then converted into an int. For example, if the 
private key was generated 2019-1-4 10:45.4561, the int returned is 20191410454561. So the new string that is feed into
the SHA256 protocol is [string given by user + time private key was created + random number between 1 and 10*100]. 
Since the random number nor the exact time and date can not be reproduced, that makes the private key generated
non-recoverable. 

## Private key to public address

This section will attempt to very briefly explain the idea of how the public addresses are generated, in this script. 
Bitcoin (BTC) and Litecoin (LTC) follow extremely, similar protocols to generate public addresses. This is 
because LTC is a hard fork from BTC. BTC and LTC addresses are formed in the major steps:

private key > SECP256k1 elliptic curve > add extension b"04" > public key
public key > SHA256 > add extension 2 > hashed public key
hashed public key > SHA256 > SHA256 > checksum
BTC/LTC address = hashed public key + checksum

The only difference between LTC and BTC addresses are that extension 2 for BTC = b"00" and for LTC = b"30".
If you want to see the theory behind this, please refer to 
https://www.freecodecamp.org/news/how-to-create-a-bitcoin-wallet-address-from-a-private-key-eca3ddd9c05f/
in the blog they give very detailed instruction on the theory behind private > address.
I did not use his code because I found his code to be rather clunky, but it is still useful to understand.

The process to make a ethereum (ETH) address is much simpler than that of BTC/LTC. The idea is basically the same, 
however, run private key through some elliptic curve and hash the result.
The major steps to form a ETH wallet are:

private key > SECP256k1 elliptic curve > public key
public key > keccak > take last 20 bytes from hash > add extension "0x" > ETH address

To implement these protocols into python, I used the package ecdsa for the SECP256k1 curve, pysha3 for the keccak
curve, and hashlib for the SHA256 hashing algorithm. Also binascii was used to decode and encode hex formatted numbers

If you wish to see the code for how this was done, please refer to https://github.com/andreshyer/OfflinePaperWallet

## Additional Notes

While this tool is safe, it is obvious that you should trust no one, especially when crypto-currency is involved. I 
would personally recommend testing a few keys that you do not intend to use on the different blockchains to make sure 
that they work fine. It is strongly encourage for you too look through the source code and make sure they are no 
obviously buggy/malicious code. The code is pretty simple, anyone can look and see there are no online sources being 
used and that I am not just sending information to myself or anyone else.

## Upcoming developments

These are changes that I would like to add in the near future. If these changes never happen, then whatever. 
1) Option for terminal tool and GUI tool
2) Option for more cryto-currencies (Most notably Monero)
    -Important to note that I am having a hard time finding a protocol for private > address for Monero (MTX)
3) Support for Linux/Mac (Mainly Linux, I do not have access to a Mac)

## Where can I donate?

You can't.
I did not make this for profit, I made this for my own needs. Since I needed a tool like this, figured others would
like it as well. I got tried of having to make secure paper wallets. Boot up a live OS, go to a site, go offline,
generate wallet, shutdown computer without going back online. That is a lot of work, I wanted something simple and
secure. Also, I learned a lot about how wallets are generated form making, which is more than enough profit for me. 
