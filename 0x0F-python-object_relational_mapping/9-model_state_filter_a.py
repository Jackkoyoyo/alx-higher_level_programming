#!/usr/bin/python3
"""
model_state_filter objects than contain a
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State)\
                        .filter(State.name.like("%a%"))\
                        .order_by(State.id):
        print("{}: {}".format(state.id, state.name))

    session.close()
