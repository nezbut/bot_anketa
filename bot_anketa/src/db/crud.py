from typing import Optional, Dict, Any

from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from .models import UserORM
from .dto import UserDTO


class UserCRUD:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_user(self, user_id: int) -> Optional[UserDTO]:
        user = await self.session.get(UserORM, user_id)
        if user:
            return UserDTO.from_orm(user)
        return None

    async def add_user(self, user: UserDTO) -> None:
        add_user = UserORM(**user.to_dict())
        self.session.add(add_user)
        await self.session.commit()

    async def update_user(self, user_id: int, update_data: Dict[str, Any]) -> None:
        stmt = update(UserORM).filter_by(id=user_id).values(**update_data)
        await self.session.execute(stmt)
        await self.session.commit()
