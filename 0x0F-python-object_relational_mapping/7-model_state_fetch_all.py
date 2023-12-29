#!/usr/bin/python3
"""
script that lists all State objects from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

 if len(argv) != 4:
        sys.exit('Use: 7-model_state_fetch_all.py <mysql username> '
                 '<mysql password> <database name>')
    engine = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
