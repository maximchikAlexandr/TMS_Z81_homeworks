from typing import Any, Dict, List

from sqlalchemy import delete, insert, select, update
from sqlalchemy.engine.base import Engine
from sqlalchemy.engine.cursor import CursorResult

from db import PostModel


class PostFacade:
    def __init__(self, engine_db: Engine):
        self.__connection = engine_db.connect()
        self.__model = PostModel

    def get_all_posts(self) -> List[Dict[str, Any]]:
        query = select(self.__model)
        cursor: CursorResult = self.__connection.execute(query)
        return cursor.mappings().all()

    def get_post(self, id_: int) -> Dict[str, Any]:
        query = select(self.__model).where(self.__model.id == id_)
        cursor: CursorResult = self.__connection.execute(query)
        return cursor.mappings().one()

    def update_post(self, id_: int, title: str, content: str) -> None:
        query = (
            update(self.__model)
            .where(self.__model.id == id_)
            .values(title=title, content=content)
        )
        self.__connection.execute(query)
        self.__connection.commit()

    def remove_post(self, id_: int) -> None:
        query = delete(self.__model).where(self.__model.id == id_)
        self.__connection.execute(query)
        self.__connection.commit()

    def create_post(self, title: str, content: str) -> None:
        query = insert(self.__model).values(title=title, content=content)
        self.__connection.execute(query)
        self.__connection.commit()


if __name__ == '__main__':
    from db import EngineDB

    e = EngineDB()
    p = PostFacade(e)
    res = p.get_all_posts()
    print(res,
          type(res),
          sep="\n")
