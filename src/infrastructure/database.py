from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQL_ALCHEMY_DATABASE_URI = "sqlite:///./src/infrastructure/todos.db"

engine = create_engine(SQL_ALCHEMY_DATABASE_URI, connect_args={'check_same_thread': False})

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()