from OTXv2 import OTXv2, IndicatorTypes
from pathlib import Path
import configparser
from datetime import datetime as dt
import json


config = configparser.ConfigParser()
config.read(Path(Path(__file__).parent).joinpath("config.ini"))
api_key = config["API"]["KEY"]

otx = OTXv2(api_key)

#pulses = otx.getall(modified_since=dt.today(),limit=5)

events = json.dumps(otx.get_pulse_details("642314b3404fb7682ccd09aa"), indent=4)

print(events)
