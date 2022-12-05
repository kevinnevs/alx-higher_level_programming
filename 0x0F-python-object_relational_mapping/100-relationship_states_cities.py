#!/usr/bin/python3
"""
Creates State "California" with the city "San Francisco"
From the database hbtn_0e_100_usa
"""
import sys
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    """create session"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """insert into query to create state California w city San Francisco"""
    new_state = State(name="California")
    new_city = City(name="San Francisco", State=new_state)
    session.add(new_state, new_city)

    """Commit the updated state and city"""
    session.commit()

    """Close session"""
    session.close()
