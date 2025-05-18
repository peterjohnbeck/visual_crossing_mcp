# visual_crossing_mcp
Basic MCP server for Visual Crossing historical weather data

Enables retrieval of historical weather data from Visual Crossing.

The Visual Crossing api is described here: https://www.visualcrossing.com/resources/documentation/weather-api/timeline-weather-api/

The MCP server can retrieve the following data for a specified location for a date or date range:

- temperature
- max temperature
- min temperature
- preciptitation
- solar radiation
- cloud cover
- snow depth
- weather type
- weather conditions
- heat index
- wind chill

First install the requirements:

```bash
pip install -r requirements.txt
```

Create or modify the .env file in the project root to read as follows:

API_KEY=XXXXXXXXXXX 

...where XXXXXXXXXXX is your API key from Visual Crossing

To enable in the Claude client, add the following to the claude_desktop_config.json file:

```json
"weather": {
      "command": "C:\\Programs\\Python\\Python311\\python.exe",
      "args": ["C:\\Path\\To\\Server\\Python\\File\\visual_crossing_mcp.py"]
    }
```
