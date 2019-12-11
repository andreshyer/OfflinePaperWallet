from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from Wallets import EthereumAP, LitecoinAP, BitcoinAP, HelpAP


class Menu_Screen(Screen):
    def __init__(self, **kwargs):
        super(Menu_Screen, self).__init__(**kwargs)
        self.soft = False


class BTC_Screen(Screen):
    def __init__(self, **kwargs):
        super(BTC_Screen, self).__init__(**kwargs)
        self.soft = True

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


class LTC_Screen(Screen):
    def __init__(self, **kwargs):
        super(LTC_Screen, self).__init__(**kwargs)
        self.soft = True

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


class ETH_Screen(Screen):
    def __init__(self, **kwargs):
        super(ETH_Screen, self).__init__(**kwargs)
        self.soft = True

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



class Help_Screen(Screen):

    def set_text(self):
        self.ids.Help_box.text = self.text

    def __init__(self, **kwargs):
        super(Help_Screen, self).__init__(**kwargs)
        self.text = HelpAP.return_help()



class Dev_Screen(Screen):
    def set_text(self):
        self.ids.Help_box.text = self.text

    def __init__(self, **kwargs):
        super(Dev_Screen, self).__init__(**kwargs)
        self.text = HelpAP.return_help()


class OfflinePaperWalletApp(App):  # Main class and starts up Kivy

    def build(self):
        self.icon = 'AppData/BTC_logo.png'
        Builder.load_file('AppData/OfflineWalletGenerator.kv')
        sm = ScreenManager()
        sm.add_widget(Menu_Screen(name='Menu_Screen'))
        sm.add_widget(BTC_Screen(name='BTC_Screen'))
        sm.add_widget(LTC_Screen(name='LTC_Screen'))
        sm.add_widget(Help_Screen(name='Help_Screen'))
        sm.add_widget(ETH_Screen(name='ETH_Screen'))
        sm.add_widget(Dev_Screen(name='Dev_Screen'))
        return sm


if __name__ == "__main__":
    OfflinePaperWalletApp().run()
