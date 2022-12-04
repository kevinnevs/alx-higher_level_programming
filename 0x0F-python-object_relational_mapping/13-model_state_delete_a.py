#!/usr/bin/python3
"""
Script that deletes state objects name with letter 'a' from db hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_state_object_a():
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                           (mysql_username, mysql_password, database_name))

    """create a session"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """insert query to add the state Louisiana"""
    states = session.query(State).filter(State.name.like("%a%")).all()

    """Delete session command"""
    for state in states:
        session.delete(state)

    """Update and commit changes"""
    session.commit()

    """closes session"""
    session.close()


if __name__ == "__main__":
    delete_state_object_a()
