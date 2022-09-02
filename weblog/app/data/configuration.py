from pydantic import BaseSettings, EmailStr

from passlib.context import CryptContext

from fastapi.security import OAuth2PasswordBearer


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


auth_scheme = OAuth2PasswordBearer(tokenUrl=f"/auth/token")


class Settings(BaseSettings):
    JWT_SECRET: str = "TEST_SECRET_DO_NOT_USE_IN_PROD"
    ALGORITHM: str = "HS256"
    # 5 minutes
    ACCESS_TOKEN_EXPIRE_TIME: int = 5

    SQLALCHEMY_DATABASE_URI: str = "postgresql://postgres:password@db:5432/app"
    ADMIN_USERNAME: str = "Admin"
    ADMIN_EMAIL: EmailStr = "admin@weblog.com"
    ADMIN_PASSWORD: str = "admin"

    class Config:
        case_sensitive = True


settings = Settings()


