from typing import Any, Callable, ParamSpec, TypeVar

P = ParamSpec("P")
T = TypeVar("T")
DecoratedCallable = TypeVar("DecoratedCallable", bound=Callable[..., Any])
