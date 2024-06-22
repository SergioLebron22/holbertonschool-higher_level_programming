#!/usr/bin/python3

"""
This script retrieves a State object from
the database based on the given state name.
If the state is found, it prints the state's ID.
Otherwise, it prints "Not found".
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sqlalchemy import insert


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    change = session.query(State).filter(State.id == 2).first()
    if change:
        change.name = 'New Mexico'
        session.commit()
