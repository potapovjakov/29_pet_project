from __future__ import annotations

from yatinder.settings.base import Base


class Prod(Base):
    DEBUG = False  # noqa: allowed straight assignment
