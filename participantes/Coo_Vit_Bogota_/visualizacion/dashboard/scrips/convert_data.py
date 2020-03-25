#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 22:28:34 2020

@author: luis.bautista
"""

from shapely.geometry import LineString, Point
import geopandas as gpd
import pandas as pd
from datetime import datetime, time

import psycopg2

import requests
import urllib 

def round_time(dt):
    if dt.minute<30:
        mins = 0
    else:
        mins = 30
    return time(dt.hour, mins, 0)

def geocode(address):
    params = {'Street':address, 'Zone':'Bogotá'}
    url = 'http://sig.simur.gov.co/arcgis/rest/services/Geocodificador/SDMColombiaPrefijo/GeocodeServer/findAddressCandidates?{}&f=pjson'.format(urllib.parse.urlencode(params))
    body  = {}
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/vnd.mds.provider+json;version=0.3',
    }

    response = requests.request("GET", url, headers=headers, data = body)
    location = response.json()
    return location

def point_from_geocode(json_data):
    loc = json_data['candidates'][0]['location']
    return Point(loc['x'], loc['y'])

str_zat = "../data/ZONAS/zat.shp"
zat = gpd.read_file(str_zat)
zat = zat [["ZAT", "geometry"]]
zat["geometry"] = zat["geometry"].centroid

str_trips = "../../data-analysis/data_outputs/viajes.csv"
trips = pd.read_csv(str_trips)

trips = trips.join(zat.set_index('ZAT'), on='zat_origen')
trips = trips.rename(columns={'geometry':'geom_origin'})

trips = trips.join(zat.set_index('ZAT'), on='zat_destino')
trips = trips.rename(columns={'geometry':'geom_destination'})
trips = trips.query('fecha.notnull()')
trips['desire_line'] = trips.apply(lambda row: LineString([row.geom_origin, row.geom_destination]), axis=1)
del trips['geom_origin']
del trips['geom_destination']
trips = gpd.GeoDataFrame(trips, geometry="desire_line")

filtered_trips = trips.query('motivo_viaje == 1 or motivo_viaje == 2 or motivo_viaje == 4')
filtered_trips = trips
filtered_trips.to_file("../data/trips.geojson", driver='GeoJSON')

trips_by_zat_origen = filtered_trips.groupby(['zat_origen'])["f_exp"].agg('sum')
trips_by_zat_origen = trips_by_zat_origen.to_frame()
trips_by_zat_origen = trips_by_zat_origen.rename(columns={'f_exp':'viajes_originados'})
trips_by_zat_origen['viajes_originados'] = trips_by_zat_origen['viajes_originados'].round(0)
trips_by_zat_destino = filtered_trips.groupby(['zat_destino'])['f_exp'].agg('sum')
trips_by_zat_destino = trips_by_zat_destino.to_frame()
trips_by_zat_destino = trips_by_zat_destino.rename(columns={'f_exp':'viajes_recibidos'})
trips_by_zat_destino['viajes_recibidos'] = trips_by_zat_destino['viajes_recibidos'].round(0)

zat = gpd.read_file(str_zat)
zat = zat [["ZAT", "geometry"]]

zat = zat.join(trips_by_zat_origen, on='ZAT')
zat = zat.join(trips_by_zat_destino, on='ZAT')

str_locations = "../../data-analysis/data_outputs/hospitales.csv"
locations = pd.read_csv(str_locations)
locations_by_zat = locations.groupby(['ZAT'])["ZAT"].agg(['count'])
locations_by_zat = locations_by_zat.rename(columns={'count':'equipamientos'})
zat = zat.join(locations_by_zat, on='ZAT')

zat = zat.fillna(0)

zat.to_file("../data/zat.geojson", driver='GeoJSON')

time_format = '%I:%M:%S %p'
trips['hora_inicio_viaje'] = trips.apply(lambda row: row.hora_inicio_viaje.replace(". ","").replace(".","").upper(), axis=1)
trips['time'] = trips.apply(lambda row: datetime.strptime(row.hora_inicio_viaje, time_format), axis=1)
trips['rounded_time'] = trips.apply(lambda row: round_time(row.time), axis=1)
trips_by_time = trips.groupby(['rounded_time'])["f_exp"].agg(['sum'])
trips_by_time['sum'] = trips_by_time['sum'].round(0)
trips_by_time_json = trips_by_time.to_json( orient='split')
trips_by_time.to_json(r'../data/time.json', orient='split')


conn = psycopg2.connect("dbname=luis.bautista user=postgres")

cur = conn.cursor()

cur.execute("SELECT * FROM covit_person;")
rows = []
for record in cur:
    rows.append(record)

cur.close()



conn.close()

rows_df = pd.DataFrame(rows, columns =['ID', 'Gender', 'Age', 'Preconditions', 'Contac_infected', 'Ocupation', 'Destination_activities', 'home_address', 'destination_address']) 
rows_df['geocode_home'] = rows_df.apply(lambda row: geocode(row.home_address), axis=1)
rows_df['geocode_destination'] = rows_df.apply(lambda row: geocode(row.destination_address), axis=1)
rows_df['desire_line'] = rows_df.apply(lambda row: LineString([point_from_geocode(row.geocode_home), point_from_geocode(row.geocode_destination)]), axis=1)
desired_trips = gpd.GeoDataFrame(rows_df, geometry="desire_line")
desired_trips.to_file("../data/desired_trips.geojson", driver='GeoJSON')

locations["geometry"] = locations.apply(lambda row: Point(row.longitud, row.latitud), axis=1)
locations = gpd.GeoDataFrame(locations)
locations.to_file("../data/locations.geojson", driver='GeoJSON')







