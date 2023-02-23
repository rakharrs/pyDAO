from person import Person
from psycopg2 import connect
from road import *
import folium

conn = connect(host='localhost',user='postgres',password='pixel',dbname='postgres')
cursor = conn.cursor()
data = []



road = Road(roadno="RNP 2")
arrayOfRoad = road.select(conn)

print(arrayOfRoad[0].start_km)
