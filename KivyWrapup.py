import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty


class Menu_Screen(Screen):
    pass


class BTC_Screen(Screen):
    pass


class LTC_Screen(Screen):
    pass


class ETH_Screen(Screen):
    pass


class Help_Screen(Screen):
    pass


class Dev_Screen(Screen):
    pass



Builder.load_file('AppData/MenuScreen.kv')
sm = ScreenManager()
sm.add_widget(Menu_Screen(name='Menu_Screen'))
sm.add_widget(BTC_Screen(name='BTC_Screen'))
sm.add_widget(LTC_Screen(name='LTC_Screen'))
sm.add_widget(ETH_Screen(name='ETH_Screen'))
sm.add_widget(Help_Screen(name='Help_Screen'))
sm.add_widget(Dev_Screen(name='Dev_Screen'))


class OfflinePaperWalletApp(App):  # Main class and starts up Kivy

    def build(self):
        self.icon = 'AppData/vcu_png.png'
        return sm


OfflinePaperWalletApp().run()
