from database.database import get_engine, get_session

def init_db():
    get_engine()
    get_session()
