from app.db.db_engine import Database
from app.db.models import Journal
from datetime import datetime


def add_students() -> None:
        session = Database().session
        session.add(Journal(date=datetime.now(),
                            first_name='Роман',
                            second_name='Собченко',
                            username='roman',
                            is_visit=True,
                            is_payed=True))
        session.add(Journal(date=datetime.now(),
                            first_name='Илья',
                            second_name='Панков',
                            username='pank',
                            is_visit=True,
                            is_payed=False))
        session.commit()