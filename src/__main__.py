from src.config import DB_USERNAME, DB_PASSWORD, DB_ADDRESS, DB_PORT
from src import dps

from mubble import Dispatch, Token, API, Mubble
from tortoise import Tortoise

dispatch = Dispatch()
for dp in dps:
    dispatch.load(dp)

token = Token.from_env(path_to_envfile=".env")
api = API(token)
bot = Mubble(api, dispatch=dispatch)


async def setup_database():
    await Tortoise.init(
        db_url=f"asyncpg://{DB_USERNAME}:{DB_PASSWORD}@{DB_ADDRESS}:{DB_PORT}/dream",
        modules={
            "models": [
                "src.database.user",
                "src.database.business",
                "src.database.supplier",
                "src.database.product",
            ]
        },
    )
    await Tortoise.generate_schemas()
    Tortoise.init_models(
        ["src.database.product", "src.database.business", "src.database.supplier"],
        "models",
    )


bot.loop_wrapper.on_startup.append(setup_database())
bot.run_forever()
