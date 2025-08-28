import json
from collections.abc import Iterable

from core import config


def serialize(*users):
    objects = users if isinstance(users, Iterable) else [users]
    root = []
    for obj in objects:
        root.append(obj.to_dict())
    return json.dumps(root)