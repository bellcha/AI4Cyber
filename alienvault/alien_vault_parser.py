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

def get_ipv4_details():


    df = pd.read_csv(Path(Path(__file__).parent).joinpath('ipv4_indicators.csv'))

    ips = [id["indicator"] for value, id in df.iterrows()]


    ip_df = pd.DataFrame(columns=['whois', 'reputation', 'indicator', 'type', 'type_title',
       'false_positive', 'validation', 'asn', 'city_data', 'city', 'region',
       'continent_code', 'country_code3', 'country_code2', 'subdivision',
       'latitude', 'postal_code', 'longitude', 'accuracy_radius',
       'country_code', 'country_name', 'dma_code', 'charset', 'area_code',
       'flag_url', 'flag_title', 'sections', 'base_indicator.id',
       'base_indicator.indicator', 'base_indicator.type',
       'base_indicator.title', 'base_indicator.description',
       'base_indicator.content', 'base_indicator.access_type',
       'base_indicator.access_reason', 'pulse_info.count', 'pulse_info.pulses',
       'pulse_info.references', 'pulse_info.related.alienvault.adversary',
       'pulse_info.related.alienvault.malware_families',
       'pulse_info.related.alienvault.industries',
       'pulse_info.related.other.adversary',
       'pulse_info.related.other.malware_families',
       'pulse_info.related.other.industries'])
    
    for i, ip in enumerate(ips):

        print(f'Gathering Indicator Details {i+1}/{len(ips)}: {ip}')

        ip_df = pd.concat([ip_df, pd.json_normalize(otx.get_indicator_details_by_section(IndicatorTypes.IPv4,ip))],ignore_index=True)

    ip_df.to_csv('ipv4_indicator_details.csv', index=False)


def get_details():
    df = pd.read_csv(Path(Path(__file__).parent).joinpath('alienvault_cobaltstrike.csv'))

    ids = [id["id"] for value, id in df.iterrows()]

    pulse_deets = pd.DataFrame(columns=['id', 'name', 'description', 'author_name', 'modified', 'created',
        'tags', 'references', 'public', 'adversary', 'targeted_countries',
        'malware_families', 'attack_ids', 'industries', 'TLP', 'indicators',
        'revision', 'groups', 'in_group', 'is_subscribing', 'author.username',
        'author.id', 'author.avatar_url', 'author.is_subscribed',
        'author.is_following'])
    
    indicator_df = pd.DataFrame(columns=['id', 'indicator', 'type', 'created', 'content', 'title', 'description', 'expiration', 'is_active'])

    for id in ids:
        #pulse_deets = pd.concat([pulse_deets,pd.DataFrame(pd.json_normalize(otx.get_pulse_details(id)))], ignore_index=True)


        for i in otx.get_pulse_details(id)['indicators']:
            indicator_df= pd.concat([indicator_df, pd.DataFrame(pd.json_normalize(i))], ignore_index=True)
        #print(pulse_deets.head())

    indicator_df.to_csv('cobaltstrike_indicators.csv', index=False)

    #pulse_deets.to_csv('pulse_ransomeware_details.csv', index=False)

#df = pd.read_csv(Path(Path(__file__).parent).joinpath('pulse_ransomeware_details.csv'))


#print(json.dumps(df['indicators'][0]))
      
#res = [json.loads(idx.replace("'", '"')) for idx in df['indicators'][0]]

#d = json.dumps("{'id': 2318, 'indicator': 'inpoucher.com', 'type': 'domain', 'created': '2015-02-20T22:54:08', 'content': '', 'title': '', 'description': '', 'expiration': None, 'is_active': 1}, {'id': 1186, 'indicator': 'kenthopm.org', 'type': 'domain', 'created': '2015-02-20T22:54:08', 'content': '', 'title': '', 'description': '', 'expiration': None, 'is_active': 1}, {'id': 1194, 'indicator': 'hevpazana.org', 'type': 'domain', 'created': '2015-02-20T22:54:08', 'content': '', 'title': '', 'description': '', 'expiration': None, 'is_active': 1}, {'id': 2319, 'indicator': 'podin.net', 'type': 'domain', 'created': '2015-02-20T22:54:08', 'content': '', 'title': '', 'description': '', 'expiration': None, 'is_active': 1}, {'id': 2320, 'indicator': 'fessleak@qip.ru', 'type': 'email', 'created': '2015-02-20T22:54:41', 'content': '', 'title': '', 'description': '', 'expiration': None, 'is_active': 1}", indent=4)

#i =json.loads(df['indicators'][0].replace("\'", "\""))

#print(i)

#idicators = [id["indicators"] for value, id in df.iterrows()]


#print(df.keys())

#print(idicators)

#print(otx.get_indicator_details_full(IndicatorTypes.FILE_PATH,indicator=295622))


#indicator = '6adef3c588ee31346fd1c6227d4203462c6788b6ca6d4b92464bbd69994b4670'

#print(pd.json_normalize(otx.get_indicator_details_full(IndicatorTypes.IPv4,'192.185.166.27')).keys())

get_details()
