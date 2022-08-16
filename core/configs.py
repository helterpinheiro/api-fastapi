from typing import List
from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
	API_V1_STR: str = '/api/v1'
	DB_URL: str = 'postgresql+asyncpg://geek:university@localhost:5432/faculdade'
	DBBasemodel = declarative_base()

	JWT_SECRET: str = '0QjkM8jKz3or4-vaOpU_bXfnqtWWNBrPJ5LXCiFQbbU'
	"""
	import secrets

	token: str = secrets.token_urlsafe(32)
	"""
	ALGORITHM: str = 'HS256'
	ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

	class Config:
		case_sensitive = True

settings: Settings = Settings()
