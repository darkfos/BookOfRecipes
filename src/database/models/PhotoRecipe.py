from src.database.create_db import MainBase
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Integer, BINARY, ForeignKey

from typing import Dict


class PhotoRecipe(MainBase):
    __tablename__ = "photorecipe"

    """ Объект - ФотоРецепта """
    id_photorec: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    photo: Mapped[bytes] = mapped_column(BINARY)
    recipe_id: Mapped[int] = mapped_column(Integer, ForeignKey("recipe.id_recipe"))
    photo = relationship("recipe", back_populates="photo_us")


    def read_model(self) -> Dict:
        """
        Чтение модели
        :return:
        """
        return {
            "id_photorec": self.id_photorec,
            "photo": self.photo,
            "id_recipe": self.recipe_id
        }