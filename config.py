# -*- coding: utf-8 -*-
"""
Конфигурация бота: загрузка переменных окружения и общие константы.
Больше никаких секретов и chat_id прямо в коде — всё берётся из
переменных окружения (или из variables.txt для локального запуска).
"""
import os
import pytz

# ============ ЧАСОВОЙ ПОЯС ============
MSK = pytz.timezone("Europe/Moscow")


def load_variables_file(path="variables.txt"):
    """Читает файл вида 'КЛЮЧ значение' (по одному на строку) и подставляет
    их в os.environ, если такая переменная ещё не задана в самом окружении.
    Реальные переменные окружения (например, заданные хостингом) всегда
    имеют приоритет над файлом."""
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(maxsplit=1)
            if len(parts) != 2:
                continue
            key, value = parts
            os.environ.setdefault(key, value)


load_variables_file()


def _parse_id_list(value: str):
    return [int(x) for x in value.split(",") if x.strip()]


# ============ ОБЯЗАТЕЛЬНЫЕ ПЕРЕМЕННЫЕ ============
# Никаких значений по умолчанию — бот не запустится, пока их не зададут.
# Так безопаснее, особенно если репозиторий когда-нибудь станет публичным.
TOKEN = os.environ["TOKEN"]
OPENWEATHER_KEY = os.environ["OPENWEATHER_KEY"]
OPENROUTER_KEY = os.environ["OPENROUTER_KEY"]
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

# ============ НАСТРОЙКИ ============
CITY = os.getenv("CITY", "Rostov-na-Donu")

# Кому приходят плановые сообщения (утро/день/вечер/тренировка/ночь).
# Поддерживается и старое имя переменной (MOM_CHAT_ID) для совместимости
# с прежним variables.txt, и новое MOM_CHAT_IDS через запятую.
_raw_mom_ids = os.getenv("MOM_CHAT_IDS") or os.getenv("MOM_CHAT_ID") or "549864131,8987266887"
MOM_CHAT_IDS = _parse_id_list(_raw_mom_ids)

# Чьи ОТВЕТЫ БОТУ дублируются в канал, и сам канал.
_raw_watch_ids = os.getenv("WATCH_USER_IDS") or "549864131,8987266887"
WATCH_USER_IDS = _parse_id_list(_raw_watch_ids)
TARGET_CHANNEL_ID = int(os.getenv("TARGET_CHANNEL_ID", "-1004360677978"))
