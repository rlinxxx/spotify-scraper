from sqlmodel import create_engine, SQLModel


DATABASE_NAME = "songs.db"
engine = create_engine(f"sqlite:///{DATABASE_NAME}")


def create_tables():
    """
    This function creates a database in SQLModel
    """
    SQLModel.metadata.create_all(engine)
