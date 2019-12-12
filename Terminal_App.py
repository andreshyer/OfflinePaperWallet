from Wallets import BitcoinAP
from Wallets import EthereumAP
from Wallets import LitecoinAP
from Wallets import HelpAP
from time import sleep


def user_input(silent):
    i = True
    while i:
        soft = True
        if silent:
            string = input("Enter Passphrase (enter in the number 2 for non-recoverable key).\n")
        else:
            string = input("Enter in a strong passphrase, this passphrase can be used to recover your private key.\n"
                           "With that said, ensure that this is a strong passphrase so others can not recover you "
                           "key.\n"
                           "If you wish to silence this warning, enter in the number '1'.\n"
                           "If you wish to have a key that can not be recovered by a word phrase, enter in the number "
                           "'2'.\n")
        if string == '2':
            while i:
                soft = False
                string = input("Non-recoverable mode is activated, use this setting with cation.\n"
                               "Enter in random keys (make it really, really long)\n")
                if len(string) < 40:
                    print('Not enough entropy, please enter more keys\n')
                else:
                    i = False

        elif string == '1':
            silent = True

        elif len(string) < 25:
            print('Not enough entropy, please enter more keys\n')

        else:
            i = False

    print()
    return string, silent, soft


WalletType = input("Welcome to the easy to use terminal tool to generate cryto-wallets offline.\n"
                   "Please enter what type of wallet you would like to generate.\n"
                   "1) Bitcoin\n"
                   "2) Ethereum\n"
                   "3) Litecoin\n"
                   "4) Help and additional information\n"
                   "5) Exit\n")

catch = False

i = True
silent = False
while i:

    if not catch:
        catch = True
    else:
        WalletType = input("\nWould you like to generate a new wallet?\n"
                           "1) Bitcoin\n"
                           "2) Ethereum\n"
                           "3) Litecoin\n"
                           "4) Help and additional information\n"
                           "5) Exit\n")

    if WalletType == str(1):
        string, silent, soft = user_input(silent)
        BitCoin_wallet = BitcoinAP.BitcoinWallet(string, soft)
        BitCoin_wallet.WalletDetails()

    elif WalletType == str(2):
        string, silent, soft = user_input(silent)
        EthereumWallet = EthereumAP.EthereumWallet(string, soft)
        EthereumWallet.WalletDetails()

    elif WalletType == str(3):
        string, silent, soft = user_input(silent)
        LitecoinWallet = LitecoinAP.LitecoinWallet(string, soft)
        LitecoinWallet.WalletDetails()

    elif WalletType == str(4):
        HelpAP.print_help()

    elif WalletType == str(5):
        print("\nThank you for using the OfflinePaperWallet!")
        sleep(3)
        i = False

    else:
        WalletType = input('Input not understood...\n'
                           "1) Bitcoin\n"
                           "2) Ethereum\n"
                           "3) Litecoin\n"
                           "4) Help and additional information\n"
                           "5) Exit\n")
