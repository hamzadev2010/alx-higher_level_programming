#!/usr/bin/python3
"""
a script that adds the State object “Louisiana”
"""
from sys import agv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    newers = State(name='Louisiana')
    session.add(newers)
    session.commit()

    print(newers.id)
