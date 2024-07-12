# In software, a data access object (DAO) is a pattern that provides an abstract interface to some type of database
# Hence, that's why we are calling the methods (functions) that are going to interact with the database a "dao"


from typing import List
from sqlmodel import Session, select
from song_model import Song 
from database import engine


def dao_get_all_songs() -> List[Song]:
    """
    In this function, we are opening a database session, in which we can run queries
    And from these queries, we are going to return all the songs
    """
    with Session(engine) as session:
        statement = select(Song)
        songs = session.exec(statement).all()
        return songs


def dao_save_songs(songs: List[Song]): 
    """
    In this function, we are opening a session, checking if the song already exists in the database
    If not, the song is stored
    """
    with Session(engine) as session:
        for song in songs:
            # Checks if the song already exists in the database by checking the id specified in the Class Song
            existing_song = session.exec(
                select(Song).where(Song.spotify_id == song.spotify_id)
            ).first()
            if not existing_song:
                session.add(song)
        session.commit()