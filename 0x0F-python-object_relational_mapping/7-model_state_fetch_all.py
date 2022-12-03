#!/usr/bin/python3
"""
Script that lists all state objects from db hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_state_obj():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    """create a session"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """query all State objects from the database"""
    states = session.query(State).order_by(State.id).all()

    """print each State object"""
    for state in states:
        print("{}: {}".format(state.id, state.name))

    """closes session"""
    session.close()


if __name__ == "__main__":
    list_state_obj()
