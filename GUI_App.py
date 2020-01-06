from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from Wallets import EthereumAP, LitecoinAP, BitcoinAP, MoneroAP, HelpAP, DevAP
from pyperclip import copy

'''
This application is backed by kivy to support a simple and easy to use GUI. Most of the code will not be explained here, 
as most of it is very repetitive. The backbone is located at 'OfflineWalletGenerator.kv' in AppData to help build the 
GUI. 
'''


class Dev_Screen(Screen):
    def set_text(self):
        self.ids.Help_box.text = self.text

    def __init__(self, **kwargs):
        super(Dev_Screen, self).__init__(**kwargs)
        self.text = DevAP.return_help()


class Menu_Screen(Screen):
    def __init__(self, **kwargs):
        super(Menu_Screen, self).__init__(**kwargs)
        self.soft = False


class Menu_Help_Screen(Screen):
    def set_text(self):
        self.ids.Help_box.text = self.text

    def __init__(self, **kwargs):
        super(Menu_Help_Screen, self).__init__(**kwargs)
        self.text = HelpAP.return_help()


class BTC_Screen(Screen):
    def __init__(self, **kwargs):
        super(BTC_Screen, self).__init__(**kwargs)
        self.soft = True

    def copy_public_key(self):
        copy(self.ids.Public_Address.text)

    def copy_private_key(self):
        copy(self.ids.Private_Key.text)

    def toggle(self):
        if self.soft:
            self.soft = False
            self.ids.NRM_state.text = "Non-\nRecoverable\nMode\n(Enabled)"
        else:
            self.soft = True
            self.ids.NRM_state.text = "Non-\nRecoverable\nMode\n(Disabled)"

    def get_keys(self):
        if len(self.ids.string_to_hash.text) < 25:
            self.ids.Public_Address.text = 'Not enough entropy, please enter more keys'
            self.ids.Private_Key.text = 'Not enough entropy, please enter more keys'
        else:
            BitcoinWallet = BitcoinAP.BitcoinWallet(str(self.ids.string_to_hash.text), self.soft)
            self.ids.Public_Address.text = BitcoinWallet.address
            self.ids.Private_Key.text = BitcoinWallet.printable_pk
            self.ids.Mnemonic_Seed.text = BitcoinWallet.readable_seed


class BTC_Help_Screen(Screen):
    def set_text(self):
        self.ids.Help_box.text = self.text

    def __init__(self, **kwargs):
        super(BTC_Help_Screen, self).__init__(**kwargs)
        self.text = HelpAP.return_help()


class LTC_Screen(Screen):
    def __init__(self, **kwargs):
        super(LTC_Screen, self).__init__(**kwargs)
        self.soft = True

    def copy_public_key(self):
        copy(self.ids.Public_Address.text)

    def copy_private_key(self):
        copy(self.ids.Private_Key.text)

    def toggle(self):
        if self.soft:
            self.soft = False
            self.ids.NRM_state.text = "Non-\nRecoverable\nMode\n(Enabled)"
        else:
            self.soft = True
            self.ids.NRM_state.text = "Non-\nRecoverable\nMode\n(Disabled)"

    def get_keys(self):
        if len(self.ids.string_to_hash.text) < 25:
            self.ids.Public_Address.text = 'Not enough entropy, please enter more keys'
            self.ids.Private_Key.text = 'Not enough entropy, please enter more keys'
        else:
            LitecoinWallet = LitecoinAP.LitecoinWallet(str(self.ids.string_to_hash.text), self.soft)
            self.ids.Public_Address.text = LitecoinWallet.address
            self.ids.Private_Key.text = LitecoinWallet.printable_pk
            self.ids.Mnemonic_Seed.text = LitecoinWallet.readable_seed


class LTC_Help_Screen(Screen):
    def set_text(self):
        self.ids.Help_box.text = self.text

    def __init__(self, **kwargs):
        super(LTC_Help_Screen, self).__init__(**kwargs)
        self.text = HelpAP.return_help()


class ETH_Screen(Screen):
    def __init__(self, **kwargs):
        super(ETH_Screen, self).__init__(**kwargs)
        self.soft = True

    def copy_public_key(self):
        copy(self.ids.Public_Address.text)

    def copy_private_key(self):
        copy(self.ids.Private_Key.text)

    def toggle(self):
        if self.soft:
            self.soft = False
            self.ids.NRM_state.text = "Non-\nRecoverable\nMode\n(Enabled)"
        else:
            self.soft = True
            self.ids.NRM_state.text = "Non-\nRecoverable\nMode\n(Disabled)"

    def get_keys(self):
        if len(self.ids.string_to_hash.text) < 25:
            self.ids.Public_Address.text = 'Not enough entropy, please enter more keys'
            self.ids.Private_Key.text = 'Not enough entropy, please enter more keys'
        else:
            EthereumWallet = EthereumAP.EthereumWallet(str(self.ids.string_to_hash.text), self.soft)
            self.ids.Public_Address.text = EthereumWallet.address
            self.ids.Private_Key.text = EthereumWallet.printable_pk
            # self.ids.Mnemonic_Seed.text = EthereumWallet.readable_seed
            self.ids.Mnemonic_Seed.text = 'Mnemonic Seed for MyEther coming soon'


class ETH_Help_Screen(Screen):
    def set_text(self):
        self.ids.Help_box.text = self.text

    def __init__(self, **kwargs):
        super(ETH_Help_Screen, self).__init__(**kwargs)
        self.text = HelpAP.return_help()


class MTX_Screen(Screen):
    def __init__(self, **kwargs):
        super(MTX_Screen, self).__init__(**kwargs)
        self.soft = True

    def copy_public_key(self):
        copy(self.ids.Public_Address.text)

    def copy_private_key(self):
        copy(self.ids.Private_Key.text)

    def copy_private_view_key(self):
        copy(self.ids.Private_View_Key.text)

    def copy_private_spend_key(self):
        copy(self.ids.Private_Spend_Key.text)

    def toggle(self):
        if self.soft:
            self.soft = False
            self.ids.NRM_state.text = "Non-\nRecoverable\nMode\n(Enabled)"
        else:
            self.soft = True
            self.ids.NRM_state.text = "Non-\nRecoverable\nMode\n(Disabled)"

    def get_keys(self):
        if len(self.ids.string_to_hash.text) < 25:
            self.ids.Public_Address.text = 'Not enough entropy, please enter more keys'
            self.ids.Private_Key.text = 'Not enough entropy, please enter more keys'
            self.ids.Private_View_Key.text = 'Not enough entropy, please enter more keys'
            self.ids.Private_Spend_Key.text = 'Not enough entropy, please enter more keys'
        else:
            MoneroWallet = MoneroAP.MoneroWallet(str(self.ids.string_to_hash.text), self.soft)
            self.ids.Public_Address.text = MoneroWallet.address
            self.ids.Private_Key.text = MoneroWallet.readable_seed
            self.ids.Private_View_Key.text = MoneroWallet.private_view_key
            self.ids.Private_Spend_Key.text = MoneroWallet.private_spend_key


class MTX_Help_Screen(Screen):
    def set_text(self):
        self.ids.Help_box.text = self.text

    def __init__(self, **kwargs):
        super(MTX_Help_Screen, self).__init__(**kwargs)
        self.text = HelpAP.return_help()


class OfflinePaperWalletApp(App):  # Main class and starts up Kivy
    def build(self):
        self.icon = 'AppData/BTC_logo.png'
        Builder.load_file('AppData/OfflineWalletGenerator.kv')
        sm = ScreenManager()

        sm.add_widget(Menu_Screen(name='Menu_Screen'))
        sm.add_widget(Menu_Help_Screen(name='Menu_Help_Screen'))

        sm.add_widget(BTC_Screen(name='BTC_Screen'))
        sm.add_widget(BTC_Help_Screen(name='BTC_Help_Screen'))

        sm.add_widget(LTC_Screen(name='LTC_Screen'))
        sm.add_widget(LTC_Help_Screen(name='LTC_Help_Screen'))

        sm.add_widget(ETH_Screen(name='ETH_Screen'))
        sm.add_widget(ETH_Help_Screen(name='ETH_Help_Screen'))

        sm.add_widget(MTX_Screen(name='MTX_Screen'))
        sm.add_widget(MTX_Help_Screen(name='MTX_Help_Screen'))

        sm.add_widget(Dev_Screen(name='Dev_Screen'))
        return sm


if __name__ == "__main__":
    OfflinePaperWalletApp().run()
