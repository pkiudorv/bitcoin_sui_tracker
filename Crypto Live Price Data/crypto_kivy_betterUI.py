from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivy.clock import Clock
import requests

KV = '''
BoxLayout:
    orientation: 'vertical'
    spacing: dp(10)
    padding: dp(20)

    MDLabel:
        text: "Bitcoin/SUI tracker"
        theme_text_color: "Primary"
        halign: "center"
        font_style: "H4"

    MDCard:
        orientation: 'vertical'
        padding: dp(15)
        size_hint: 1, None
        height: dp(120)
        elevation: 8
        radius: [20,]

        MDLabel:
            id: btc_label
            text: "Bitcoin (BTC): Loading..."
            theme_text_color: "Secondary"
            font_style: "H5"
            halign: "center"

    MDCard:
        orientation: 'vertical'
        padding: dp(15)
        size_hint: 1, None
        height: dp(120)
        elevation: 8
        radius: [20,]

        MDLabel:
            id: sui_label
            text: "Sui (SUI): Loading..."
            theme_text_color: "Secondary"
            font_style: "H5"
            halign: "center"

    MDRaisedButton:
        text: "Check Prices"
        pos_hint: {"center_x": 0.5}
        on_press: app.get_crypto_prices()
'''

class CryptoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.theme_style = "Dark"  # Change to "Light" if you prefer
        Clock.schedule_interval(self.get_crypto_prices, 10)  # Auto-refresh every 10 sec
        return Builder.load_string(KV)

    def get_crypto_prices(self, *args):
        try:
            url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,sui&vs_currencies=eur"
            response = requests.get(url)
            data = response.json()

            btc_price = data["bitcoin"]["eur"]
            sui_price = data["sui"]["eur"]

            self.root.ids.btc_label.text = f"Bitcoin (BTC): €{btc_price}"
            self.root.ids.sui_label.text = f"Sui (SUI): €{sui_price}"
        except Exception as e:
            self.root.ids.btc_label.text = "Error fetching data"
            self.root.ids.sui_label.text = str(e)

if __name__ == "__main__":
    CryptoApp().run()
