from __future__ import annotations

from configurations.values import BooleanValue

from yatinder.settings.dev import Dev


class Test(Dev):
    ALLOWED_HOSTS = ['*']  # noqa: allowed straight assignment

    DEBUG = BooleanValue(True)
