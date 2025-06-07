from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QCheckBox, QListView, QVBoxLayout
from PyQt5.QtCore import QStringListModel, QTimer
from ui_currency_converter import Ui_Form
import sys
import datetime

class CurrencyApp(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("სავალუტო გადამცვლელი")
        self.currencies = {
            "USD" : "US Dollar" , "EUR": "Euro", "GEL": "Georgian Lari", "GBP": "British Pound",
            "TRY": "Turkish Lira", "RUB": "Russian Ruble", "AZN": "Azerbaijan Manat", "AMD": "Armenian Dram",
             "IRR": "Iranian Rial", "INR": "Indian Rupee", "UAH": "Ukrainian Hryvnia", "PLN": "Polish Zloty",
            "BYN": "Belarusian Ruble", "ILS": "Israeli New Shekel", "KZT": "Kazakhstani Tenge",
            "UZS": "Uzbekistani Sum", "CZK": " Czech Koruna", "CAD": "Canadian Dollar",
            "AUD": "Australian Dollar", "NZD": "New Zealand Dollar", "BRL": "Brazilian Real",
            "ARS": "Argentine Peso", "EGP": "Egyptian Pound", "MXN": "Mexican Peso", "AED": "Emirati Dirham",
            "SAR": "Saudi Arabian Riyal", "QAR": "Qatari Rial", "KWD": "Kuwaiti Dinar", "DKK":"Danish Krone",
            "SEK": "Swedish Krona", "NOK": "Norwegian Krone","HUF": "Hungarian Forint" ,"RON": " Romanian Leu",
            "BGN": "Bulgarian Lev", "ZAR": "South African Rand", "IDR": "Indonesian Rupiah", "SGD": "Singapore Dollar",
            "JPY": "Japanese Yen", "KRW": "South Korean Won", "CNY": " Chinese Yuan Renminbi", "CHF": "Swiss Franc"
                           }


        self.comboBox_from.addItems([
            "USD", "EUR", "GEL", "GBP", "TRY", "RUB", "AZN", "AMD", "IRR", "INR", "UAH", "PLN",
            "BYN","ILS","KZT","UZS","CZK","CAD","AUD","NZD","BRL", "ARS", "EGP", "MXN", "AED", "SAR",
            "QAR", "KWD", "DKK", "SEK", "NOK","HUF","RON", "BGN", "ZAR", "IDR","SGD" ,"JPY", "KRW","CNY","CHF"])
        self.comboBox_to.addItems([
            "USD", "EUR", "GEL", "GBP", "TRY", "RUB", "AZN", "AMD", "IRR", "INR", "UAH", "PLN",
            "BYN", "ILS", "KZT","UZS" ,"CZK", "CAD", "AUD", "NZD" ,"BRL", "ARS", "EGP", "MXN","AED","SAR",
            "QAR","KWD", "DKK", "SEK", "NOK","HUF","RON", "BGN", "ZAR", "IDR" ,"SGD","JPY", "KRW", "CNY", "CHF"])


        self.convert_button.clicked.connect(self.convert_currency)


        self.round_checkbox = QCheckBox("მრგვალი შედეგი")
        self.layout().addWidget(self.round_checkbox)

        # Add QListView to display recent conversions
        self.list_view = QListView()
        self.conversion_model = QStringListModel()
        self.conversion_history = []
        self.list_view.setModel(self.conversion_model)
        self.layout().addWidget(self.list_view)

        # Add QTimer to update time in QLabel
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every second

        self.time_label = self.result_label  # reuse the QLabel
        self.update_time()


        usd_rates = {
        "USD": 1.0, "EUR": 0.87, "GEL": 2.73, "GBP": 0.73, "TRY": 39.21, "RUB": 78.55, "AZN": 1.7, "AMD": 383.33,
        "IRR": 41739, "INR": 85.77, "UAH": 41.46, "PLN": 3.76, "BYN": 3.27, "ILS": 3.5, "KZT": 510.06, "UZS": 12804.27,
        "CZK": 21.74, "CAD": 1.36, "AUD": 1.54, "NZD": 1.66, "BRL": 5.56, "ARS": 1180.56, "EGP": 49.43, "MXN": 19.11,
        "AED": 3.67, "SAR": 3.75, "QAR": 3.64, "KWD": 0.31, "DKK": 6.54, "SEK": 9.64, "NOK": 10.11, "HUF": 354.18,
        "RON": 4.42, "BGN": 1.71, "ZAR": 17.77, "IDR": 16309.01, "SGD": 1.28, "JPY": 144, "KRW": 1359,
            "CNY": 7.19, "CHF": 0.82
        }


        self.rates = {}
        for from_curr in usd_rates:
            self.rates[from_curr] = {}
            for to_curr in usd_rates:
                self.rates[from_curr][to_curr] = usd_rates[to_curr] / usd_rates[from_curr]

    def update_time(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.time_label.setText(f"დრო: {current_time}")

    def convert_currency(self):
        try:
            amount = float(self.input_amount.text())
            from_curr = self.comboBox_from.currentText()
            to_curr = self.comboBox_to.currentText()

            if from_curr == to_curr:
                result = amount
            else:
                result = amount * self.rates[from_curr][to_curr]

            if self.round_checkbox.isChecked():
                result = round(result)

            result_text = f"{amount} {from_curr} = {result:.2f} {to_curr}"
            self.result_label.setText(result_text)

            self.conversion_history.append(result_text)
            self.conversion_model.setStringList(self.conversion_history[-5:])  # Last 5 entries

        except ValueError:
            QMessageBox.warning(self, "შეცდომა", "გთხოვთ შეიყვანეთ რიცხვი.")
        except KeyError:
            QMessageBox.warning(self, "შეცდომა", "კურსი არ მოიძებნა მითითებული ვალუტებისთვის.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CurrencyApp()
    window.show()
    sys.exit(app.exec_())
