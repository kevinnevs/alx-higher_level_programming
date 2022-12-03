#!/usr/bin/python3
"""
Script that lists all state objects that has letter a from db hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def filter_state_obj_a():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    """create a session"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """query all State objects from the database"""
    states = session.query(State).filter(State.name.contains('a')
                                         ).order_by(State.id)

    """print each State object"""
    for state in states:
        print("{}: {}".format(state.id, state.name))

    """closes session"""
    session.close()


if __name__ == "__main__":
    filter_state_obj_a()
