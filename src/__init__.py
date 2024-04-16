from src import commands
from src import middlewares

dps = [*commands.dps, *middlewares.dps]


__all__ = ["dps"]
