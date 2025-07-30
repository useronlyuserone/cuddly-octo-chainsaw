# Weather App 🌤️

A command-line weather application that fetches current weather data from the OpenWeatherMap API.

## Features

- Get current weather for any city worldwide
- Display temperature in Celsius
- Show weather description and humidity
- Clean, formatted output with emojis
- Error handling for invalid cities and network issues

## Prerequisites

- Python 3.6 or higher
- OpenWeatherMap API key (free at https://openweathermap.org/api)

## Installation

1. Clone this repository or download the files
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Get your free API key from [OpenWeatherMap](https://openweathermap.org/api)

4. Set your API key as an environment variable:
   ```bash
   export OPENWEATHER_API_KEY=your_api_key_here
   ```

## Usage

### Basic usage:
```bash
python weather_app.py London
python weather_app.py "New York"
python weather_app.py Tokyo
```

### Using API key as argument:
```bash
python weather_app.py --api-key your_key_here Paris
```

### Running the example script:
```bash
python example_usage.py
```

### Example output:
```
🔍 Fetching weather data for 'London'...

🌤️  Weather in London, GB
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🌡️  Temperature: 15.2°C (feels like 14.8°C)
🌦️  Condition: Partly Cloudy
💧 Humidity: 72%
```

## Error Handling

The app handles various error scenarios:
- Invalid city names
- Network connectivity issues
- Missing API key
- API rate limits
- Malformed API responses

## API Key Setup

You can provide your API key in two ways:

1. **Environment Variable (Recommended):**
   ```bash
   export OPENWEATHER_API_KEY=your_api_key_here
   ```

2. **Command Line Argument:**
   ```bash
   python weather_app.py --api-key your_key_here CityName
   ```

## License

This project is open source and available under the [MIT License](LICENSE).
