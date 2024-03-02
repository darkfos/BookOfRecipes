import datetime

from src.database.create_db import MainBase
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Integer, String, DATE, ForeignKey

from typing import NewType, Any, Dict


class Recipe(MainBase):
    __tablename__ = "recipe"

    """ Объект - рецепт """
    id_recipe: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title_recipe: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    complexity: Mapped[str] = mapped_column(String, default="легкий")
    time_cook: Mapped[int] = mapped_column(Integer, default=10)
    date_create: Mapped[datetime.datetime] = mapped_column(DATE, default=datetime.datetime.now().date())

    # Таблица Photo
    photo_us = relationship("photorecipe", back_populates="photo")

    # Таблица User
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id_user"))
    recipes = relationship("user", back_populates="user_post")


    def read_model(self) -> Dict:
        """
        Чтение модели
        :return:
        """
        return {
            "id_recipe": self.id_recipe,
            "title_recipe": self.title_recipe,
            "description": self.description,
            "complexity": self.complexity,
            "time_cook": self.time_cook,
            "date_create": self.date_create,
            "id_user": self.user_id
        }