import json
import os
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from keyboards import search_menu
from aiogram.filters import Command

command_router = Router()

# Шлях до файлу з даними користувачів
users_file = "users.json"

# Функція для збереження користувача у файл
def save_user_data(user_id, username, first_name):
    try:
        # Завантажуємо існуючі дані
        with open("users.json", "r", encoding="utf-8") as f:
            users = json.load(f)
    except FileNotFoundError:
        # Якщо файл не існує, створюємо порожній список
        users = []

    # Перевіряємо, чи користувач уже є у списку
    for user in users:
        if user["id"] == user_id:
            return  # Якщо користувач уже є, не додаємо його знову

    # Додаємо нового користувача
    users.append({
        "id": user_id,
        "username": username,
        "first_name": first_name
    })

    # Зберігаємо оновлені дані у файл
    with open("users.json", "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)

@command_router.message(CommandStart())
async def start_command(message: Message):
    """
    Обробник команди /start.
    """
    # Зберігаємо дані користувача
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    save_user_data(user_id, username, first_name)

    # Відправляємо відповідь користувачу
    await message.answer(
        f"Привіт, {message.from_user.first_name}! 👋\n"
        "Я допоможу тобі збірати підписників з каналу в список телеграм💬\n"
        "по кнопці ниже⬇️ ти можеш подивитися весь функціонал Бота🌟\n"
        "\n", reply_markup=search_menu,
    )


@command_router.callback_query(F.data == "info")
async def cmd_info(callback: CallbackQuery):
    await callback.answer('info')
    await callback.message.answer(f"Функціонал Бота🤖 \n"
                                  "\n"
                                  "по команді /parser [силка на канал] ⚠️ обов'язково канал має бути відкритим \n"
                                  "\n"
                                  "по команді /piplist парсінг пройшов успішно то ви можете получити список по цій команді✅\n"
                                  "\n"
                                  "по команді /clear ви очищаєте список це потрібно робити для того щоби список видавався коректно\n"
                                  "\n"
                                  "по команді /help ви можете написати в підтримку за конкретною інформацією або підтримкою\n"
                                  "\n"
                                  "Щоби получити доступ до функцій⚠️ /parser , /piplist вам потрібно звязатися з адміністарцією\n"
                                  "ви це можете зробити через команду /help \n"
                                  )







# Список ID адміністраторів
ADMINS = [1332517469 , 6395768505] # Замість цих ID вставте реальні ID ваших адміністраторів

@command_router.message(Command("list"))
async def command_piplist(message: Message):
    # Перевірка чи користувач є адміном
    if message.from_user.id in ADMINS:
        await message.answer(
            "Command - /start 'запуск і перезапуск бота'\n"
            "\n"
            "Command - /help 'Підтримка в боті'\n"
            "\n"
            "Command - /sendall 'команда для розсилки-реклами'\n"
            "\n"
            "Command - /piplist 'видання підписників у списку'\n"
            "\n"
            "Command - /clear 'очищення списку підписників'\n"
            "\n"
            "Command - /reply 'відповідь на проблему тільки адмінам!'\n"
            "\n"
            "Command - /list 'подивитися список команди' \n"
            "\n"
            "Command - /admin 'адмін панель для легкого використання'\n"
            "\n"
            "Commаnd - /add ID 'видає права на доступ до функцій /parser'\n"
            "\n"
            "Commаnd - /addoff ID 'забирає доступ до функцій /parser'\n"
            "\n"
            "Commаnd - /online 'по цій команді ви можете переглянути активність користувачів в боті'\n"
            "\n"
            "Commаnd - /maintenance 'по цій команді ви можете запустити автоматичну перевірку бота щоби оникнути помилок'\n"
            "\n"
            "Commаnd - /list_users 'ця команда показує вам всю кількість людей в боті з бази даних'\n"
            "\n"
            "Commаnd - /addinfo 'переглянути всі активні сеанси на доступ до /parser'\n"
            "\n")
    else:
        await message.answer("У вас немає доступу до цієї команди. ❌")