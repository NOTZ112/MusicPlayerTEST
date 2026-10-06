"""
Music Player, Telegram Voice Chat Bot

Based on the upstream MusicPlayer project.
License: GNU Affero General Public License v3.0.
Keep the upstream LICENSE and required notices with this project.
"""

import os
from dotenv import load_dotenv

load_dotenv()


def _bool_env(name: str, default: bool = False) -> bool:
    value = os.environ.get(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


class Config:
    def __init__(self) -> None:
        self.API_ID = os.environ.get("API_ID")
        self.API_HASH = os.environ.get("API_HASH")
        self.SESSION = os.environ.get("SESSION")
        self.BOT_TOKEN = os.environ.get("BOT_TOKEN")

        self.SUDOERS = [
            int(user_id)
            for user_id in os.environ.get("SUDOERS", "").split()
            if user_id.lstrip("-").isdigit()
        ]

        if not self.SESSION or not self.API_ID or not self.API_HASH:
            raise RuntimeError("SESSION, API_ID and API_HASH are required")

        self.SPOTIFY = bool(
            os.environ.get("SPOTIFY_CLIENT_ID")
            and os.environ.get("SPOTIFY_CLIENT_SECRET")
        )
        self.QUALITY = os.environ.get("QUALITY", "high").lower()
        self.PREFIXES = os.environ.get("PREFIX", "!").split()
        self.LANGUAGE = os.environ.get("LANGUAGE", "en").lower()
        self.STREAM_MODE = (
            "audio"
            if os.environ.get("STREAM_MODE", "audio").lower() == "audio"
            else "video"
        )
        self.ADMINS_ONLY = _bool_env("ADMINS_ONLY", False)
        self.SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
        self.SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")


config = Config()
