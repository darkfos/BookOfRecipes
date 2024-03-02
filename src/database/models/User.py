from src.database.create_db import MainBase
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Integer, String, DATE

from typing import Dict


class User(MainBase):
    """
    Объект - User
    """

    id_user: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name_user: Mapped[str] = mapped_column(String, nullable=False)
    email_user: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String(35))
    date_reg: Mapped[DATE] = mapped_column(DATE)
    user = relationship("Recipe", back_populates="recipes")

    def read_model(self) -> Dict:
        """
        Чтение модели
        :return:
        """
        return {
            "id_user": self.id_user,
            "name_user": self.name_user,
            "email_user": self.name_user,
            "password": self.password,
            "date_reg": self.date_reg
        }