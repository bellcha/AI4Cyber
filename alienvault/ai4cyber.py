from OTXv2 import OTXv2, IndicatorTypes
from pathlib import Path
import configparser
from datetime import datetime, timedelta
import pandas as pd
import json


config = configparser.ConfigParser()
config.read(Path(Path(__file__).parent).joinpath("config.ini"))
api_key = config["API"]["KEY"]

otx = OTXv2(api_key)

mtime = (datetime.now() - timedelta(days=30)).isoformat()

pulses = otx.search_pulses('BlackCat Ransomware')

#pulses = otx.get_pulse_details('554a4723b45ff50cc4d77959')

print(pulses)

#print(json.dumps(pulses, indent=4))

##events = otx.getevents_since(mtime)

df = pd.DataFrame(pulses['results'])

#file_name = pulses['id']

df.to_csv(f'alienvault_blackcat_ransomware.csv', index=False)

#print(df)


