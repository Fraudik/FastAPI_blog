import sqlalchemy

metadata = sqlalchemy.MetaData()

users_table = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(60)),
    sqlalchemy.Column("email", sqlalchemy.String(256), unique=True, index=True),
    sqlalchemy.Column("login", sqlalchemy.String(30), unique=True, index=True),
    sqlalchemy.Column("password", sqlalchemy.String()),
)
