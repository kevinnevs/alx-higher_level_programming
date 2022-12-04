#!/usr/bin/python3
"""
Script that changes the state objects name from db hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def update_state_object():
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                           (mysql_username, mysql_password, database_name))

    """create a session"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """insert query to add the state Louisiana"""
    state = session.query(State).filter_by(id=2).first()

    """Update the state name"""
    if state:
        state.name = "New Mexico"

    """Update and commit changes"""
    session.commit()

    """closes session"""
    session.close()


if __name__ == "__main__":
    update_state_object()
