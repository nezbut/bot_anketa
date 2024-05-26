from sqlalchemy.ext.asyncio import AsyncSession

from .models import UserORM
from .dto import UserDTO


class UserCRUD:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_user(self, user_id: int):
        return await self.session.get(UserORM, user_id)

    async def add_user(self, user: UserDTO):
        add_user = UserORM(**user.to_dict())
        self.session.add(add_user)
        await self.session.commit()
