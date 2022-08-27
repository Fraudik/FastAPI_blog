import sqlalchemy
from sqlalchemy.dialects.postgresql import UUID

from models.users import users_table

metadata = sqlalchemy.MetaData()

auth_tokens_table = sqlalchemy.Table(
    "auth_tokens",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("token",
                      UUID(as_uuid=False), server_default=sqlalchemy.text("uuid_generate_v4()"),
                      nullable=False,
                      unique=True, index=True),
    sqlalchemy.Column("expires", sqlalchemy.DateTime()),
    sqlalchemy.Column("user_id", sqlalchemy.ForeignKey(users_table.c.id)),
)
