# Weather Forecasting Python Application

<h3>Overview</h3>
<p>This simple weather forecast application/GUI was created with PyQt5 and Python. By entering the name of the city, users can utilise the OpenWeatherMap API to retrieve the most recent weather information.</p>

<h3>Features</h3>
<ul>
    <li>GUI created using PyQt5</li>
    <li>Fetches current weather information</li>
    <li>Shows the city name, temperature (°C), and weather description</li>
    <li>Using Error handling caused by incorrect city names or API malfunctions</li>
</ul>

<h3>Prerequisites</h3>
<p>Make sure you have Python installed (version 3.6+ recommended). You also need to install the following dependencies:</p>
<pre>
pip install PyQt5 requests
</pre>

<h3>Installation and Running the Program</h3>
<ol>
    <li>Clone the repository:</li>
    <pre>
    git clone https://github.com/aman-mishra01/weather-forecasting-python
    </pre>
    <li>Navigate to the project directory:</li>
    <pre>
    cd weather-forecasting-python
    </pre>
    <li>Create a virtual environment (optional but recommended):</li>
    <pre>
    python -m venv venv
    </pre>
    <li>Activate the virtual environment:</li>
    <pre>
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    </pre>
    <li>Install the required dependencies:</li>
    <pre>
    pip install -r requirements.txt
    </pre>
    <li>Run the application:</li>
    <pre>
    python weather_forecast.py
    </pre>
</ol>

<h3>API Key Configuration</h3>
<p>This application uses the OpenWeatherMap API. Replace the <code>api_key</code> variable in the script with your own API key. You can obtain a free API key by signing up at <a href="https://home.openweathermap.org/users/sign_up" target="_blank">OpenWeatherMap</a>.</p>

<h3>File Structure</h3>
<ul>
    <li><code>weather_forecast.py</code> - Main application script</li>
    <li><code>README.md</code> - Documentation for the project</li>
</ul>

<h3>Example Output</h3>
<pre>
City: New York
Temperature (°C): 15.2
Description: Clear sky
</pre>

<h3>License</h3>
<p>This project is open-source and available under the MIT License.</p>

<h3>Author</h3>
<p>Aman Mishra</p>