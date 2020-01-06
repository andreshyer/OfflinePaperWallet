

text = '''
General Help:
To navigate to different sections, simply click the buttons to navigate the
GUI. When generating wallets, the user is required to type text into the
large text box above where the private key and public address boxes are
located. The text entered is a passphrase that get converted into the
private keys and public addresses shown (With the exception of Monero). 
That is why is it important to have a really strong passphrase, as others 
could recover your wallet if you have a predictable passphrase. 

What is 'Non-recovery Mode'?:
OfflinePaperWallet gives the user the option to create private keys and
public addresses that can not be recovered from a passphrase. Use this
option with cation. If you ever lose your private key, you will not be
able to recover your funds. But, this option can be used as a more
secure method of generating paper wallets. Using this option adds more
entropy than the user provides. If you want to see how this was
implemented, please refer to Developer Information.

Public Address vs Private Key (Bitcoin, Litecoin, Ethereum):
The public address that gets generated is the address that you want to share
with others. With the public address, people can send you cryto that matches
the wallet generated. The private key can be used to recover the funds from
your wallet. The private key can be swept into most hot wallets, such as
Electrum.

Mnemonic Seed vs public address (Monero):
Monero operates differently than the other cryto-currencies on in this app.
That is because it was built to make the block chain truly anonymous.
The exact details I will not discuss here. If you wish to learn more,
please refer to https://www.getmonero.org/get-started/faq/. A Monero paper
wallet works similarly to a other paper wallets. You have people send you
funds to you public address, as with the other cryto-currencies. But, 
instead of using a private key to swept funds into wallets, you use the 
seed to recovery your wallet. Then you can access your funds for the 
wallet once recovered. So the Mnemonic seed acts as the private key.

Where to keep Private keys and Public addresses?:
As the name of this application suggest, it is highly recommended that you
write your private key on paper. Please do not save your private key to
your desktop, that is how you get your funds stolen either by a hacker or
simply a clever co-worker. Your public address you can, and should, freely 
share with others. The public address you can store on your desktop :D.
If you do decide to key your private keys on any sort of hardware, including
flash drives, it is strongly encouraged for you to encrypt the files. You
can use PGP or Veracrypt for this propose. 

How do I know the wallets are being made correctly and securely?:
Good question, and this can lead into a detailed discussion. If you want to
know exactly how the wallets are being generated (such as protocols, and how
they was implemented into python), please refer to Developer Information.
If want to know whether or not the wallets are being generated correctly,
you can use blockchains to test your addresses and keys. Use a test
private key you do not intend to key crypto on, and see if the public
address matches to what the blockchain has. 

General Notes:
There are many features missing in this application that other popular 
wallets have, such as Electrum or MyMonero. This was done on propose, 
this is a minimalistic application. OfflinePaperWallet is meant to be 
run from a computer that does not need an internet connection, with the 
sole propose of generating private keys and public addresses for common 
crypto-currencies. The main propose of this application is to generate 
offline-paper wallet where the user can store large amounts of cryto 
without needing to go through a JS website or bootup a live OS. It is 
still recommended to use an air-gaped machine, however, for very large 
amounts of cryto.
'''


def print_help():
    print(text)

def return_help():
    return text
