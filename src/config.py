from envparse import env

env.read_envfile(".env")

GOOGLE_SEARCH_TOKEN = env.str("GOOGLE_SEARCH_TOKEN")

DB_USERNAME = env.str("DB_USERNAME")
DB_PASSWORD = env.str("DB_PASSWORD")
DB_ADDRESS = env.str("DB_ADDRESS")
DB_PORT = env.int("DB_PORT")
