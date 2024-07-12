from sqlmodel import Field, SQLModel


class Song(SQLModel, table = True):
    """
    The Class Song inherits from the SQL Model
    :params: table: means that this class should be trated as a representation of a database table
    """
    id: int = Field(default = None, primary_key = True)
    title: str
    album: str
    artist: str
    spotify_id: str

