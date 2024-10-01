from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from setting import DB_USER, DB_PASSWORD, DB_LOCALHOST, DB_NAME
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@localhost:{DB_LOCALHOST}/{DB_NAME}"

Base = declarative_base()


class Manufacturer(Base):
    __tablename__ = 'manufacturer'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    aircraft_models = relationship('AircraftModels', back_populates='manufacturer')


class AircraftModels(Base):
    __tablename__ = 'aircraft_model'
    id = Column(Integer, primary_key=True)
    model_description = Column(String, nullable=False)
    manufacturer_id = Column(Integer, ForeignKey('manufacturer.id'), nullable=False)
    manufacturer = relationship('Manufacturer', back_populates='aircraft_models')

    __table_args__ = (
        UniqueConstraint("manufacturer_id", "model_description", name="uix_manufacturer_id_model_description"),
    )


try:
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
except:
    print("Не удалось запустить приложение из-за проблем с базой данных")


