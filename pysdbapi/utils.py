from collections import OrderedDict
from typing import Optional

from .type_hints import CursorAlias


def get_list_ordereddict(cursor: CursorAlias) -> Optional[list[OrderedDict]]:
    if cursor.description:
        columns: list[str] = [column[0] for column in cursor.description]
        return [OrderedDict(zip(columns, row)) for row in cursor.fetchall()]
    return None
