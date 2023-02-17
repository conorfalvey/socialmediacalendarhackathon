from sqlalchemy import create_engine


class DatabaseContext(object):
    def __init__(self):
        self.engine = create_engine(
            "postgresql+psycopg2://postgres:hackathonsocialcal@localhost:5433/postgres"
        )
