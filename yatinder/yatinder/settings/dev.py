from __future__ import annotations

from configurations.values import BooleanValue

from yatinder.settings.base import Base


class Dev(Base):
    ALLOWED_HOSTS = ['*']  # noqa: allowed straight assignment

    DEBUG = BooleanValue(True)
