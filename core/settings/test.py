from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent
environ.Env.read_env(BASE_DIR / ".env.test")

from .base import *
