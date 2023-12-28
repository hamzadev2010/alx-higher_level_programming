#!/usr/bin/python3
""" script that prints the first State object from the database"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()
    state = session.query(State).order_by(State.id).first()
     if states is None:
        print ("Nothing")
    else:
        print("{}: {}".format(states.id, states.name))
