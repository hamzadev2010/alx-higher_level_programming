#!/usr/bin/python3
"""
script that lists all State objects that contain the letter a from the database
"""
from sys import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    st = session.query(State).filter(State.name.like('%a%')).all()

       for state in st:
        print("{}: {}".format(state.id, state.name))
