from src.database.create_db import MainBase
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Integer, BINARY, ForeignKey

from typing import Dict


class PhotoRecipe(MainBase):
    """
        Объект - ФотоРецепта
    """

    id_photorec: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    photo: BINARY = mapped_column(BINARY)
    id_recipe: Mapped[int] = mapped_column(Integer, ForeignKey("Recipe.id_recipe"))
    photo = relationship("Recipe", back_populates="photo_us")


    def read_model(self) -> Dict:
        """
        Чтение модели
        :return:
        """
        return {
            "id_photorec": self.id_photorec,
            "photo": self.photo,
            "id_recipe": self.id_recipe
        }