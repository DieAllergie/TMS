from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///test.db", echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    count = Column(Integer)
    comment = Column(String(50))

    def __init__(self, name, price, count, comment):
        self.name = name
        self.price = price
        self.count = count
        self.comment = comment


Base.metadata.create_all(engine)


def add_to_base(obj: Products):
    session.add(obj)
    session.commit()


def del_from_base(n):
    obj = session.query(Products).get(n)
    if obj:
        session.delete(obj)
        session.commit()
    else:
        print(f'В таблице отсуствует запись с id={n}')


def update_on_id(n):
    obj = session.query(Products).get(n)
    name = input('Введите новое значение name или нажмите enter, чтобы оставить прежнее: ')
    if name:
        obj.name = name
    price = input('Введите новое значение price или нажмите enter, чтобы оставить прежнее: ')
    if price:
        obj.price = int(price)
    count = input('Введите новое значение count или нажмите enter, чтобы оставить прежнее: ')
    if count:
        obj.count = int(count)
    comment = input('Введите новое значение comment или нажмите enter, чтобы оставить прежнее: ')
    if comment:
        obj.comment = comment
    session.commit()


def show_table():
    obj = session.query(Products.id, Products.name, Products.price, Products.comment).all()
    for i in obj:
        print(i)


apple = Products('apple', 20, 10, 'apple from village')
milk = Products('milk', 20, 10, 'apple from village')


def main():
    # update_on_id(7)
    # del_from_base(2)
    show_table()
    # add_to_base(apple)


if __name__ == '__main__':
    main()
