from layout import app_layout

class scraper:
    def __init__(self):
        self.app = True

    def main(self):
        self.layout = app_layout()
        self.window = self.layout.main()

app = scraper()
app.main()