from OTXv2 import OTXv2, IndicatorTypes
from pathlib import Path
import configparser
from datetime import datetime as dt
import pandas as pd


config = configparser.ConfigParser()
config.read(Path(Path(__file__).parent).joinpath("config.ini"))
api_key = config["API"]["KEY"]

otx = OTXv2(api_key)

pulses = otx.getall()

df = pd.read_json(pulses)

df.to_csv('alienvault.csv')


