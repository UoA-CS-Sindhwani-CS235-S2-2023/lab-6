from abc import ABC
from typing import List

from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.exc import NoResultFound

from games.adapters.repository import AbstractRepository
from games.adapters.utils import search_string
from games.domainmodel.model import Game, Publisher, Genre, User, Review


class SessionContextManager:
    def __init__(self, session_factory):
        self.__session_factory = session_factory
        self.__session = scoped_session(self.__session_factory)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    @property
    def session(self):
        return self.__session

    def commit(self):
        self.__session.commit()

    def rollback(self):
        self.__session.rollback()

    def reset_session(self):
        # this method can be used e.g. to allow Flask to start a new session for each http request,
        # via the 'before_request' callback
        self.close_current_session()
        self.__session = scoped_session(self.__session_factory)

    def close_current_session(self):
        if not self.__session is None:
            self.__session.close()


class SqlAlchemyRepository(AbstractRepository, ABC):

    def __init__(self, session_factory):
        self._session_cm = SessionContextManager(session_factory)

    def close_session(self):
        self._session_cm.close_current_session()

    def reset_session(self):
        self._session_cm.reset_session()

    # region Game_data
    def get_games(self) -> List[Game]:
        games = self._session_cm.session.query(Game).order_by(Game._Game__game_id).all()
        return games

    def get_game(self, game_id: int) -> Game:
        game = None
        try:
            game = self._session_cm.session.query(
                Game).filter(Game._Game__game_id == game_id).one()
        except NoResultFound:
            print(f'Game {game_id} was not found')

        return game

    def add_game(self, game: Game):
        with self._session_cm as scm:
            scm.session.merge(game)
            scm.commit()

    def add_multiple_games(self, games: List[Game]):
        with self._session_cm as scm:
            for game in games:
                scm.session.merge(game)
            scm.commit()

    def get_number_of_games(self):
        total_games = self._session_cm.session.query(Game).count()
        return total_games

    # endregion

    # region Publisher data
    def get_publishers(self) -> List[Publisher]:
        pass

    def add_publisher(self, publisher: Publisher):
        with self._session_cm as scm:
            scm.session.merge(publisher)
            scm.commit()

    def add_multiple_publishers(self, publishers: List[Publisher]):
        with self._session_cm as scm:
            for publisher in publishers:
                scm.session.merge(publisher)
            scm.commit()

    def get_number_of_publishers(self) -> int:
        pass

    # endregion

    # region Genre_data
    def get_genres(self) -> List[Genre]:
        pass

    def add_genre(self, genre: Genre):
        with self._session_cm as scm:
            scm.session.merge(genre)
            scm.commit()

    def add_multiple_genres(self, genres: List[Genre]):
        with self._session_cm as scm:
            for genre in genres:
                scm.session.merge(genre)
            scm.commit()

    # endregion

    def search_games_by_title(self, title_string: str) -> List[Game]:
        pass
