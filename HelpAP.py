

text = '''
------------------------------------------------------------------------------------------------------------------------
OfflinePaperWallet is not sponsored or owned by any developer of Bitcoin, Ethereum, or Litecoin. That means this is an
unofficial application, and should be validated by experienced users. I will provide information on how this
application works, and why it is safe to use. There are a few different offline tools that do serve a similar propose
to what this provides. The difference is that here I will try and explain how the private keys and public addresses are
being generated. Hopefully this can provide confidence that this is a safe tool to use.
------------------------------------------------------------------------------------------------------------------------

General Help:
This is a terminal tool, meaning that commands must be typed. Typing in the number '3' will lead to option 3 being
executed. There is not much else to really explain. If you can read this, then the application is working just fine.

General Information:
All the private key and public address that generated in application are generated using python built-in packages as
well as the external packages: ecdsa, base58, and pysha3. Also this application is completely self-contained. Meaning
the machine never has to be connected to the internet for this application to work. Also, all the source code for this
application is available at

Non-recoverable Mode:
When generating a new addresses, the option for 'non-recoverable' is available. By default, the private keys
generated are recovered by the passphrase provided by the user. The reason for this is that the passphrase the user
provides is converted into a private by the SHA_256 protocol.

'''


def print_help():
    print(text)