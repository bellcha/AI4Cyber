from __future__ import annotations
import requests as rq
import configparser
from pathlib import Path
import pandas as pd
from pydantic import BaseModel, Field
from typing import Optional


class Location(BaseModel):
    country: str
    region: str
    timezone: str


class As(BaseModel):
    asn: int
    name: str
    route: str
    domain: str
    type: str


class IP(BaseModel):
    ip: str
    location: Location
    as_: Optional[As] = Field(None, alias='as')
    isp: str

config = configparser.ConfigParser()
config.read(Path(Path(__file__).parent).joinpath("config.ini"))

api_key = config["API"]["IP"]


csv_file = Path(Path(__file__).parent).joinpath("Indicator_Details/alienvault_ipv4.csv")

df = pd.read_csv(csv_file)

ip_address = list(df['indicator'])

#print(ip_address)

with open('ip_geo_location.csv', 'w') as f:
    f.write('ip,country,region\n')

    for ip in ip_address[47:]:


        url = 'https://geo.ipify.org/api/v2/country'

        params = {'apiKey':api_key, 'ipAddress':ip}

        try:

            response = IP(**rq.get(url, params=params).json())

            f.write(f'{response.ip},{response.location.country},{response.location.region}\n')
        
        except Exception as err:
            print(err)

