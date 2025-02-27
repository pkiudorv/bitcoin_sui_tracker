import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.core.window import Window

# Set Window size
Window.size = (350, 500)

class CryptoApp(App):
    def build(self):
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=20)
        
        # Title
        self.title_label = Label(text="Crypto Price Checker", font_size=24, bold=True)
        self.layout.add_widget(self.title_label)

        # Crypto Labels
        self.btc_label = Label(text="Bitcoin (BTC): Loading...", font_size=18)
        self.sui_label = Label(text="Sui (SUI): Loading...", font_size=18)
        
        self.layout.add_widget(self.btc_label)
        self.layout.add_widget(self.sui_label)

        # Button to Check Prices
        self.check_button = Button(text="Check Prices", font_size=18, size_hint=(1, 0.2))
        self.check_button.bind(on_press=self.get_crypto_prices)
        self.layout.add_widget(self.check_button)

        # Auto-refresh prices every 10 seconds
        Clock.schedule_interval(self.get_crypto_prices, 10)

        return self.layout

    def get_crypto_prices(self, *args):
        try:
            url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,sui&vs_currencies=eur"
            response = requests.get(url)
            data = response.json()
            
            # Update Labels
            btc_price = data["bitcoin"]["eur"]
            sui_price = data["sui"]["eur"]

            self.btc_label.text = f"Bitcoin (BTC): €{btc_price}"
            self.sui_label.text = f"Sui (SUI): €{sui_price}"

        except Exception as e:
            self.btc_label.text = "Error fetching data"
            self.sui_label.text = str(e)

# Run the App
if __name__ == "__main__":
    CryptoApp().run()
