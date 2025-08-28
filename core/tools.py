import json
from collections.abc import Iterable
from pathlib import Path

from core import objects


def serialize(*users):
    objects = users if isinstance(users, Iterable) else [users]
    root = []
    for obj in objects:
        root.append(obj.to_dict())
    return json.dumps(root)


def deserialize(fname):
    fpath = Path(fname)
    users_data = None
    with open(fpath, "r") as data:
        users_data = json.load(data)
    users = []
    for user_data in users_data["users"]:
        users.append(objects.User.from_dict(user_data))
    return users
