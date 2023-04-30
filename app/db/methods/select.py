from app.db.db_engine import Database
from app.db.models import Journal


def select_all_students():
    session = Database().session
    result = session.query(Journal).all()
    session.close()
    return result

def select_all_students_who_not_payed():
    session = Database().session
    result = session.query(Journal).filter_by(is_payed=False).one()
    session.close()
    return result

