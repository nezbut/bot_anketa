from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class UserORM(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    age: Mapped[int]
    gender: Mapped[str]
    city: Mapped[str]
