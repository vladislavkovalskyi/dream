from envparse import env

env.read_envfile(".env")

SERPER_NEWS_API = env.str("SERPER_NEWS_API")

DB_USERNAME = env.str("DB_USERNAME")
DB_PASSWORD = env.str("DB_PASSWORD")
DB_ADDRESS = env.str("DB_ADDRESS")
DB_PORT = env.int("DB_PORT")
