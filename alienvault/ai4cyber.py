from OTXv2 import OTXv2, IndicatorTypes
from pathlib import Path
import configparser
from datetime import datetime as dt
import pandas as pd


config = configparser.ConfigParser()
config.read(Path(Path(__file__).parent).joinpath("config.ini"))
api_key = config["API"]["KEY"]

otx = OTXv2(api_key)

pulses = otx.search_pulses('bank')

df = pd.DataFrame(pulses['results'])

df.to_csv('alienvault_banking.csv')

print(df.head())


