from sqlalchemy import Column, Integer, String, Float, Boolean, Date, Time
from app.db.db_engine import Database
from json import dumps as json_dumps


class Products(Database.BASE):

    # имя таблицы
    __tablename__ = 'journal'

    # колонки
    id = Column(Integer, primary_key=True)
    date = Column(Date) # дата тренировки
    first_name = Column(String) # Имя
    second_name = Column(String) # Фамилия
    username = Column(String, index=True) # telegram username
    is_visit = Column(Boolean) # посетил или нет
    is_payed = Column(Boolean) # оплачено или нет

    # при запросе данных получаем структуру json строки
    def __repr__(self) -> json_dumps:
        # json string
        return json_dumps({'id': self.id,
                           'date': self.date,
                           'first_name': self.first_name,
                           'second_name': self.second_name,
                           'username': self.username,
                           'is_visit': self.is_visit,
                           'is_payed': self.is_payed})
    

def register_models():
    Database.BASE.metadata.create_all(Database().engine)