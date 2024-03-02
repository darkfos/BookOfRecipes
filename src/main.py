#Home directory
from src.database.create_db import create_database

#Models
from src.database.models.Recipes import Recipe
from src.database.models.PhotoRecipe import PhotoRecipe
from src.database.models.User import User

#Other directory
import asyncio

if __name__ == "__main__":
    #Запуск проекта
    asyncio.run(create_database())