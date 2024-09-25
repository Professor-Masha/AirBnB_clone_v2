# db_storage.py

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBStorage:
    """This class manages storage of hbnb models in database"""
    
    def __init__(self):
        """Create the engine and session"""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}/{database}', pool_pre_ping=True)
        self.__session = None

    def reload(self):
        """Create all tables in the database and initialize session"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

