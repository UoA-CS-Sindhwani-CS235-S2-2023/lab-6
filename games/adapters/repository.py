import abc
from typing import List

from games.domainmodel.model import Game, Publisher, Genre, Review, User

repo_instance = None


class RepositoryException(Exception):
    def __init__(self, message=None):
        print(f'RepositoryException: {message}')


class AbstractRepository(abc.ABC):

    # region Publisher_data
    @abc.abstractmethod
    def add_publisher(self, publisher: Publisher):
        """ Add a single game to the repository of games. """
        raise NotImplementedError

    @abc.abstractmethod
    def add_multiple_publishers(self, publisher: List[Publisher]):
        """ Add multiple games to the repository of games. """
        raise NotImplementedError

    def get_publisher(self, publisher_name: str) -> Publisher:
        """ Returns the list of games. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_publishers(self) -> List[Publisher]:
        """ Returns the list of games. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_number_of_publishers(self):
        """ Returns a number of games exist in the repository. """
        raise NotImplementedError

    # endregion

    # region games_data
    @abc.abstractmethod
    def add_game(self, game: Game):
        """ Add a single game to the repository of games. """
        raise NotImplementedError

    @abc.abstractmethod
    def add_multiple_games(self, games: List[Game]):
        """ Add multiple games to the repository of games. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_game(self, game_id: int) -> Game:
        """ Returns the list of games. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_games(self) -> List[Game]:
        """ Returns the list of games. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_number_of_games(self):
        """ Returns a number of games exist in the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def search_games_by_title(self, title_string: str) -> List[Game]:
        """Search for the games whose title includes the parameter title_string.
        It searches for the game title in case-insensitive and without trailing space.
        For example, the title 'Call of Duty' will be searched if the title_string is 'duty'. """
        raise NotImplementedError

    # endregion

    # region Genre
    @abc.abstractmethod
    def get_genres(self, genre: Genre) -> List[Genre]:
        """ Return all genres that exist in the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def add_genre(self, genre: Genre):
        """ Add a genre to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def add_multiple_genres(self, genres: List[Genre]):
        """ Add many genres to the repository. """
        raise NotImplementedError
    # endregion

