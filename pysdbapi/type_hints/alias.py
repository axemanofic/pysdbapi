from typing import Any, Optional, OrderedDict, TypeAlias, Union

CursorAlias: TypeAlias = Any

PrettyTableAlias: TypeAlias = Any

QueryResult: TypeAlias = Optional[list[OrderedDict]]

ExecutorResult: TypeAlias = Union[QueryResult, PrettyTableAlias]
