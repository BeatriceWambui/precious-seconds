class Config:
    SECRET_KEY="exrctfvygbhnjkmfgvbhfghbngh"
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:E*7@wach@localhost/pitching'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}