from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateDrinkRequest(_message.Message):
    __slots__ = ["description", "name", "price"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    description: str
    name: str
    price: float
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., price: _Optional[float] = ...) -> None: ...

class DeleteDrinkRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteDrinkResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Drink(_message.Message):
    __slots__ = ["description", "id", "name", "price"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    description: str
    id: str
    name: str
    price: float
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., price: _Optional[float] = ...) -> None: ...

class GetDrinkRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ListDrinksRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListDrinksResponse(_message.Message):
    __slots__ = ["drinks"]
    DRINKS_FIELD_NUMBER: _ClassVar[int]
    drinks: _containers.RepeatedCompositeFieldContainer[Drink]
    def __init__(self, drinks: _Optional[_Iterable[_Union[Drink, _Mapping]]] = ...) -> None: ...

class UpdateDrinkRequest(_message.Message):
    __slots__ = ["description", "id", "name", "price"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    description: str
    id: str
    name: str
    price: float
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., price: _Optional[float] = ...) -> None: ...
