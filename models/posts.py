import sqlalchemy

from models.users import users_table

metadata = sqlalchemy.MetaData()

posts_table = sqlalchemy.Table(
    "posts",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("datetime", sqlalchemy.DateTime()),
    sqlalchemy.Column("title", sqlalchemy.String(100)),
    sqlalchemy.Column("text", sqlalchemy.Text()),
    sqlalchemy.Column("user_id", sqlalchemy.ForeignKey(users_table.c.id)),
)
