import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTextEdit, QLineEdit, QVBoxLayout, QMessageBox
from dotenv import dotenv_values

class WeatherForecastApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Weather Forecast")
        self.setGeometry(100, 100, 400, 300)
        
        self.city_label = QLabel("Enter City:")
        self.city_field = QLineEdit()
        
        self.fetch_button = QPushButton("Fetch Weather")
        self.fetch_button.clicked.connect(self.fetch_weather)
        
        self.weather_area = QTextEdit()
        self.weather_area.setReadOnly(True)
        
        layout = QVBoxLayout()
        layout.addWidget(self.city_label)
        layout.addWidget(self.city_field)
        layout.addWidget(self.fetch_button)
        layout.addWidget(self.weather_area)
        
        self.setLayout(layout)
    
    def fetch_weather(self):
        city = self.city_field.text().strip()
        # Visit https://openweathermap.org/api to generate your own api key. 
        api_key = dotenv_values(".env")["API_KEY"]
        api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                self.display_weather(self.parse_weather(response.json()))
            else:
                self.weather_area.setText("City not found")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Error fetching weather data: {e}")
    
    def parse_weather(self, json_data):
        try:
            city = json_data["name"]
            temperature = json_data["main"]["temp"]
            description = json_data["weather"][0]["description"]
            
            weather_info = (
                f"City: {city}\n"
                f"Temperature (°C): {temperature}\n"
                f"Description: {description}\n"
            )
            return weather_info
        except KeyError:
            return "Error parsing weather data"
    
    def display_weather(self, weather_info):
        self.weather_area.setText(weather_info)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WeatherForecastApp()
    window.show()
    sys.exit(app.exec_())
