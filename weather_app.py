#!/usr/bin/env python3
"""
Command-line weather app that fetches weather data from OpenWeatherMap API.
Usage: python weather_app.py <city_name>
"""

import sys
import requests
import argparse
from typing import Dict, Any


class WeatherApp:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    def get_weather(self, city: str) -> Dict[str, Any]:
        """
        Fetch weather data for the given city.
        
        Args:
            city (str): Name of the city
            
        Returns:
            Dict containing weather data
            
        Raises:
            requests.RequestException: If API request fails
            KeyError: If expected data is missing from response
        """
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'  # Use Celsius
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()  # Raise an exception for bad status codes
            
            data = response.json()
            
            # Check if the city was found
            if data.get('cod') != 200:
                raise ValueError(f"City '{city}' not found. Please check the spelling.")
            
            return data
            
        except requests.exceptions.RequestException as e:
            raise requests.RequestException(f"Failed to fetch weather data: {e}")
    
    def format_weather_info(self, weather_data: Dict[str, Any]) -> str:
        """
        Format weather data into a readable string.
        
        Args:
            weather_data (Dict): Raw weather data from API
            
        Returns:
            str: Formatted weather information
        """
        try:
            city = weather_data['name']
            country = weather_data['sys']['country']
            temperature = weather_data['main']['temp']
            feels_like = weather_data['main']['feels_like']
            humidity = weather_data['main']['humidity']
            description = weather_data['weather'][0]['description'].title()
            
            weather_info = f"""
🌤️  Weather in {city}, {country}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🌡️  Temperature: {temperature}°C (feels like {feels_like}°C)
🌦️  Condition: {description}
💧 Humidity: {humidity}%
            """
            
            return weather_info.strip()
            
        except KeyError as e:
            raise KeyError(f"Missing expected data in weather response: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Get current weather information for a city",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python weather_app.py London
  python weather_app.py "New York"
  python weather_app.py Tokyo

Note: You need to set your OpenWeatherMap API key as an environment variable:
  export OPENWEATHER_API_KEY=your_api_key_here
  
Get your free API key at: https://openweathermap.org/api
        """
    )
    
    parser.add_argument(
        'city',
        help='Name of the city to get weather for'
    )
    
    parser.add_argument(
        '--api-key',
        help='OpenWeatherMap API key (can also be set via OPENWEATHER_API_KEY env var)'
    )
    
    args = parser.parse_args()
    
    # Get API key from argument or environment variable
    api_key = args.api_key
    if not api_key:
        import os
        api_key = os.getenv('OPENWEATHER_API_KEY')
    
    if not api_key:
        print("❌ Error: OpenWeatherMap API key is required!")
        print("\nYou can provide it in two ways:")
        print("1. Set environment variable: export OPENWEATHER_API_KEY=your_key")
        print("2. Use --api-key argument: python weather_app.py --api-key your_key CityName")
        print("\nGet your free API key at: https://openweathermap.org/api")
        sys.exit(1)
    
    # Create weather app instance
    weather_app = WeatherApp(api_key)
    
    try:
        # Fetch weather data
        print(f"🔍 Fetching weather data for '{args.city}'...")
        weather_data = weather_app.get_weather(args.city)
        
        # Display formatted weather information
        weather_info = weather_app.format_weather_info(weather_data)
        print(weather_info)
        
    except ValueError as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
    except requests.RequestException as e:
        print(f"❌ Network Error: {e}")
        sys.exit(1)
    except KeyError as e:
        print(f"❌ Data Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()