#!/usr/bin/python3

"""
This script fetches all cities and their
corresponding states from a database using SQLAlchemy.
"""

import sys
from model_state import Base, State
from model_city import Base, City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sqlalchemy import insert


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    states = session.query(State).order_by(State.id).all()
    cities = session.query(City).order_by(City.id).all()

    for state in states:
        for city in cities:
            if city.state_id == state.id:
                print(f"{state.name}: ({city.id}) {city.name}")\

    session.close()
