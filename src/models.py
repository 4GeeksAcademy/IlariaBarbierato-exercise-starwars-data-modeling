import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Planets(Base):
    __tablename__ = "planets"
    id = Column(Integer, primary_key = True)
    name = Column(String(50), unique = True)
    population = Column(Integer)
    climate = Column(String(30))
    diameter = Column(Float)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key = True)
    name = Column(String(50), unique = True)
    birth_year = Column(Integer)
    gender = Column(String(20))
    height = Column(Float)
    eye_color = Column(String(15))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet_id_relationship = relationship(Planets)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key = True)
    name = Column(String(50), unique = True)
    model = Column(String(20))

class VehiclesPilots(Base):
    __tablename__ = 'vehicles_pilots'
    id = Column(Integer, primary_key = True)
    character_id = Column(Integer, ForeignKey('characters.id'))
    character_id_relationship = relationship(Characters)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicle_id_relationship = relationship(Vehicles)

class FavoritesCharacters(Base):
    __tablename__ = 'favorites_characters'
    id = Column(Integer, primary_key = True)
    character_id = Column(Integer, ForeignKey('characters.id'))
    character_id_relationship = relationship(Characters)

class FavoritesPlanets(Base):
    __tablename__ = 'favorites_planets'
    id = Column(Integer, primary_key = True)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet_id_relationship = relationship(Planets)

class FavoritesVehicles(Base):
    __tablename__ = 'favorites_vehicles'
    id = Column(Integer, primary_key = True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicle_id_relationship = relationship(Vehicles)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
