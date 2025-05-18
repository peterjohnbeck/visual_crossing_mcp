import json
import requests
from typing import List
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import os

load_dotenv()
mcp = FastMCP("historical_weather")


API_KEY = os.getenv("API_KEY")
base_url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/history?'

def build_url(location, start_date, end_date, unit_of_measure):

    aggregate_hours = '&aggregateHours=24'
    contentType = '&contentType=json'

    startDateTime = '&startDateTime=' + start_date
    endDateTime = '&endDateTime=' + end_date
    unitGroup = '&unitGroup=' + unit_of_measure
    location = '&location=' + location
    key = '&key=' + API_KEY

    # return base_url + location +'/' + date + '/' + date + '?unitGroup='+ unit_of_measure + '&key=' + API_KEY + '&contentType=json'
    return base_url + aggregate_hours+ startDateTime + endDateTime + unitGroup + contentType + location + key

@mcp.tool()
def visual_crossing_history(location, start_date, end_date, unit_of_measure) -> dict:

    """
    Search for historical weather information from the Visual Crossing weather API

    Take the location, start and end dates, and a unit of measure (metric or us)

    Return a dict with the date 
        * temperature
        * max temperature
        * min temperature
        * preciptitation
        * solar radiation
        * humidity
        * cloud cover
        * snow depth
        * weather type
        * weather conditions
        * heat index
        * wind chill

    """
    response = requests.get(build_url(location=location, start_date=start_date, end_date=end_date,unit_of_measure=unit_of_measure))

    if response.status_code == 200:
        weather_dict = {}
        for weather_record in response.json()['locations'][location]['values']:
            date_dict = {}
            date_dict["temperature"] = weather_record["temp"]
            date_dict["max_temperature"] = weather_record["maxt"]
            date_dict["min_temperature"] = weather_record["mint"]
            date_dict["precipitation"] = weather_record["precip"]
            date_dict["solar_radiation"] = weather_record["solarradiation"]
            date_dict["humidity"] = weather_record["humidity"]
            date_dict["cloud_cover"] = weather_record["cloudcover"]
            date_dict["snow_depth"] = weather_record["snowdepth"]
            date_dict["weather_type"] = weather_record["weathertype"]
            date_dict["weather_conditions"] = weather_record["conditions"]
            date_dict["heat_index"] = weather_record["heatindex"]
            date_dict["windchill"] = weather_record["windchill"]
            weather_dict[str(weather_record['datetimeStr'])] = date_dict           
            #weather_dict[str(weather_record['datetimeStr'])] = str(weather_record['temp'])
        return weather_dict 
    else:
        return {}    

if __name__ == "__main__":
    mcp.run(transport='stdio')

    