from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
from resources import CheckCurrentWeather, CheckCityWeather, DriveStatus

app = Flask(__name__)
api = Api(app)


## Main API
api.add_resource(CheckCurrentWeather, '/v1/api/checkCurrentWeather')  # '/v1/api/checkCurrentWeather' is our entry point
#api.add_resource(CheckCityWeather, '/v1/api/checkCityWeather/<city_name>')  # '/v1/api/checkCityWeather' is our entry point
api.add_resource(DriveStatus, '/v1/api/driveStatus')  # '/v1/api/driveStatus' is our entry point

if __name__ == '__main__':
    app.run(port=88)

