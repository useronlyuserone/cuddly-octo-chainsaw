#!/usr/bin/env python3
"""
Example usage of the WeatherApp class.
This demonstrates how to use the weather app programmatically.
"""

import os
from weather_app import WeatherApp


def main():
    # Example of using the WeatherApp class directly
    print("🌤️  Weather App - Example Usage")
    print("=" * 40)
    
    # Check if API key is available
    api_key = os.getenv('OPENWEATHER_API_KEY')
    if not api_key:
        print("❌ Please set your OPENWEATHER_API_KEY environment variable")
        print("Example: export OPENWEATHER_API_KEY=your_api_key_here")
        return
    
    # Create weather app instance
    weather_app = WeatherApp(api_key)
    
    # List of cities to demonstrate
    cities = ["London", "New York", "Tokyo", "Paris", "Sydney"]
    
    for city in cities:
        try:
            print(f"\n🔍 Fetching weather for {city}...")
            weather_data = weather_app.get_weather(city)
            weather_info = weather_app.format_weather_info(weather_data)
            print(weather_info)
            print("-" * 40)
            
        except Exception as e:
            print(f"❌ Error getting weather for {city}: {e}")
            continue


if __name__ == "__main__":
    main()