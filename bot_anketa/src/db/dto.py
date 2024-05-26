from typing import Dict, Any
from dataclasses import dataclass

from .models import UserORM


@dataclass
class UserDTO:
    id: int
    name: str
    age: int
    gender: str
    city: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "city": self.city,
        }

    @classmethod
    def from_orm(cls, user: UserORM) -> "UserDTO":
        return cls(
            id=user.id,
            name=user.name,
            age=user.age,
            gender=user.gender,
            city=user.city
        )
