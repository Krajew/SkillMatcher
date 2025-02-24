from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

from utils.variable import DatabaseVariable 

def create_engin(user, password, host, port, db_name):
    url = f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
    engine = create_engine(url)

    if not database_exists(engine.url):
        create_database(engine.url)

    return engine

def get_engine():
    keys = ['db_user', 'db_pass', 'db_host', 'db_port', 'db_name']
    if not all(key in keys for key in DatabaseVariable):
        raise Exception("Invalid config file, check utils/variable.py.")
    
    return create_engin(DatabaseVariable['db_user'],
                    DatabaseVariable['db_pass'],
                    DatabaseVariable['db_host'],
                    DatabaseVariable['db_port'],
                    DatabaseVariable['db_name'])

def get_session():
    engine = get_engine()
    session = sessionmaker(bind=engine)
    return session
