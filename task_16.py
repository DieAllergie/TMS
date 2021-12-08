from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy_utils import database_exists
from sqlalchemy_utils import create_database
from sqlalchemy.sql.schema import ForeignKey


DB_USER = 'postgres'
DB_PASSWORD = 'powerpost1404'
DB_NAME = 'test'

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}', echo=True)

if not database_exists(engine.url):
    create_database(engine.url)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Brand(Base):
    __tablename__ = 'brand'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    def __init__(self, name):
        self.name = name


class Car(Base):
    __tablename__ = 'car'
    id = Column(Integer, primary_key=True)
    model = Column(String(25), nullable=False)
    release_year = Column(Integer, nullable=False)
    brand = Column(String, ForeignKey('brand.name'), nullable=False)
    brand_name = relationship('Brand', foreign_keys='Car.brand')


Base.metadata.create_all(engine)

def main():
    # brand1 = Brand(name='WV')
    car1 = Car(model='tuareg', release_year=2019, brand='WV')
    # car2 = Car(model='tiguan', release_year=2020, brand=brand1)

    session.add_all([car1])

    session.commit()


if __name__ == '__main__':
    main()


