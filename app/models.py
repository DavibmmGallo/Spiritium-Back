from dataclasses import dataclass
from dacite import from_dict
from datetime import datetime
from uuid import uuid4

@dataclass
class MongoBase:
    _id: str
    created_at: datetime
    updated_at: datetime

    @classmethod
    def new(cls, data: dict):
        return from_dict(
            data_class=cls,
            data={
                '_id': str(uuid4()),
                'created_at': datetime.utcnow(),
                'updated_at': datetime.utcnow(),
                **data
            }
        )


@dataclass
class Article(MongoBase):
    title: str
    author: str
    description: str
    release_date: datetime
    text: str

@dataclass
class User(MongoBase):
    name: str
    email: str
    password: str