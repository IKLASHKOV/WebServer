from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Manufacturer(Base):
    __tablename__ = 'manufacturer'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    aircraft_models = relationship('AircraftModels', back_populates='manufacturer')


class AircraftModels(Base):
    __tablename__ = 'aircraft_model'
    id = Column(Integer, primary_key=True)
    model_code = Column(String, nullable=False)
    model_description = Column(String, nullable=False)
    manufacturer_id = Column(Integer, ForeignKey('manufacturer.id'))
    manufacturer = relationship('Manufacturer', back_populates='aircraft_models')
