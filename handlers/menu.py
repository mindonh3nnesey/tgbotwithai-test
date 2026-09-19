# -*- coding: utf-8 -*-
"""
Навигация по меню: /start, /help и переключение между категориями.
"""
from telegram import Update
from telegram.ext import ContextTypes

from keyboards import (
    main_menu_keyboard,
    style_menu_keyboard,
    ai_menu_keyboard,
    media_menu_keyboard,
)

WELCOME_TEXT = (
    "👋 Привет, мамуля! 💖\n\n"
    "Я твой личный помощник! Выбирай категорию на клавиатуре снизу:\n\n"
    "🔹 🎨 Стиль дня — цвета на сегодня/завтра и аффирмации\n"
    "🔹 🧠 Помощник — любой вопрос к ИИ\n"
    "🔹 🌤 Погода — что на улице прямо сейчас\n"
    "🔹 📥 Медиа — скачать рилс/фото из Instagram\n\n"
    "Всё то же самое работает и командами — набери /help, если забудешь.\n\n"
    "Я всегда рядом и люблю тебя! ❤️"
)

HELP_TEXT = (
    "📋 Команды:\n"
    "/start — начать / показать меню\n"
    "/menu — вернуться в главное меню\n"
    "/colors — цвета дня\n"
    "/colors_tomorrow — цвета на завтра\n"
    "/affirmation — аффирмация\n"
    "/weather — погода\n"
    "/ai — спросить ИИ\n"
    "/insta — скачать из Instagram\n"
    "/clear — очистить историю ИИ\n\n"
    "Либо просто пользуйся кнопками снизу 💖"
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_TEXT, reply_markup=main_menu_keyboard())


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP_TEXT, reply_markup=main_menu_keyboard())


async def show_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Главное меню:", reply_markup=main_menu_keyboard())


async def show_style_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎨 Стиль дня:", reply_markup=style_menu_keyboard())


async def show_ai_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🧠 Помощник:", reply_markup=ai_menu_keyboard())


async def show_media_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📥 Медиа:", reply_markup=media_menu_keyboard())
