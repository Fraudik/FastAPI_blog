#  Copyright (c)  2022 Fraudik (Blinov Ilya)

import typing

from sqlalchemy.ext.declarative import as_declarative, declared_attr


class_registry: typing.Dict = {}


@as_declarative(class_registry=class_registry)
class Base:
    id: typing.Any
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()
