## Module for resources
from flask import request
from flask_restful import Resource
import json
import requests
import ipapi
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps


class CheckCurrentWeather(Resource):

    def get(self):
        if 'current_city' in request.args:
            current_city = request.args["current_city"]
            city = current_city
        else:
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
