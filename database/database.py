from .models import *
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import select,delete
import sqlalchemy

Base.metadata.create_all(engine)
ss = Session(engine,autoflush=False)



def get_selection(sel):
    return ss.scalars(select(sel)).all()
def get_selection2(sel):
    return ss.query(sel).all()

def del_selection(name: str, sel, fil):
    if (name.__len__()<2): return
    ss.delete(ss.query(sel).filter(fil == name).first())
    ss.commit()

def del_by_id(id, sel):
    if (id is None): return
    ss.delete(ss.query(sel).all()[id])
    ss.commit()




def add_city(name: str):
    if (ss.query(Cities).filter(Cities.city_Name == name).first()): return
    ss.add(Cities(city_Name= name))
    ss.commit()

def add_stat(name: str, city):
    c = get_selection2(Cities)[city]
    if (c is None): return
    if (ss.query(Stations).filter(Stations.station_Name == name, Stations.city == c).first()): return
    ss.add(Stations(station_Name=name, city=c))
    ss.commit()

def add_route(name: str):
    if (ss.query(Routes).filter(Routes.route_Name == name).first()): return
    ss.add(Routes(route_Name= name))
    ss.commit()

def add_point(route, stat, time):
    r = get_selection2(Routes)[route]
    s = get_selection2(Stations)[stat]
    if (ss.query(RoutesStructure).filter(RoutesStructure.route == r, RoutesStructure.station == s, RoutesStructure.time == time).first()): return
    ss.add(RoutesStructure(route=r, station=s, time=time))
    ss.commit()

def add_type(name: str, speed: int):
    if (ss.query(TransportTypes).filter(TransportTypes.type_Name == name, TransportTypes.type_Average_Speed == speed).first()): return
    ss.add(TransportTypes(type_Name=name, type_Average_Speed= speed))
    ss.commit()

def add_transport(date: datetime, type):
    t = get_selection2(TransportTypes)[type]
    ss.add(Transport(commissioning_date=date, type=t))
    ss.commit()

def change_transport_route(ts, route):
    t = get_selection2(Transport)[ts]
    if route is None:
        t.route = None
    else:
        r = get_selection2(Routes)[route]
        t.route = r
    ss.commit()