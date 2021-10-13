## Module for resources
from flask import request
from flask_restful import Resource
import json


class CheckCurrentWeather(Resource):

    pass


class CheckCityWeather(Resource, city_name):

    pass

class DriveStatus(Resource, drive_status):

    pass