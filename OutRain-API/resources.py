## Module for resources
from flask import request
from flask_restful import Resource
import json
import ipapi
from pyowm import OWM



class CheckCurrentWeather(Resource):

    def get(self):
        location_dict = ipapi.location()
        city = location_dict["city"]
        country = location_dict["country"]
        owm = OWM('6613b8f7387ec9c7de8c0d1e107583a2')
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(city)
        weather = observation.weather
        temp = weather.temperature('celsius')["temp"]
        weather_dict = {"city": city, "country": country, "degrees": temp}
        return weather_dict
    pass


class CheckCityWeather(Resource):

    def get(self):
        current_city = request.args.get('city_name')
        strarr = list(current_city)
        for i, c in enumerate(strarr):
            if c == ' ':
                strarr[i] = '%20'
        city = "".join(strarr)
        owm = OWM('6613b8f7387ec9c7de8c0d1e107583a2')
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(city)
        weather = observation.weather
        temp = weather.temperature('celsius')["temp"]
        location = observation.to_dict()
        country = location['location']['country']
        weather_dict = {"city": city, "country": country, "degrees": temp}
        return weather_dict
    pass


class DriveStatus(Resource):

    def get(self):
        drives_status_dict = {}
        drives_online_dict = {}
        drives_offline_dict = {}
        with open('input.json', 'r') as f:
            data = json.load(f)
        for key in data.keys():
            current_dict = dict()
            response_dict = list(data[key].split(','))
            for index, value in enumerate(response_dict):
                current_value = value.split()
                key = current_value[0]
                value = current_value[1]
                current_dict[key] = value
            name = current_dict['name']
            status = current_dict['status']
            drives_status_dict[name] = current_dict
            if status == 'Online':
                drives_online_dict[name] = current_dict
            elif status == 'Offline':
                drives_offline_dict[name] = current_dict
        if 'drive_status' in request.args:
            drive_status = request.args["drive_status"]
            if drive_status == 'Online':
                return drives_online_dict
            elif drive_status == 'Offline':
                return drives_offline_dict
        else:
            return drives_status_dict
    pass

    def post(self):
        json_data = request.form #should be request.get_json() - not working
        with open('container.json', 'w', encoding='utf-8') as f:
            json.dump(json_data, f)
        return json_data
    pass
