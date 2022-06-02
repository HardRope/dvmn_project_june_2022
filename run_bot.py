import os

from dotenv import load_dotenv
from telegram.ext import Updater
from telegram.ext import CommandHandler

from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


def start(update, context):
    global admins
    user_name = update.effective_user.name

    if user_name in admins:
        invite_text = f"Добро пожаловать, {user_name}. Ты - админ"
    else:
        invite_text = f"Добро пожаловать, {user_name}. Ты - ученик"

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=invite_text
    )


def admin_button(update, context):
    keyboard = [
        [
            KeyboardButton('Загрузить учеников'),
            KeyboardButton('Загрузить ПМ-ов')
        ]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    update.message.reply_text("Админка", reply_markup=reply_markup)


def user_button(update, context):
    keyboard = [
        [
            KeyboardButton('Выбрать удобное время'),
            KeyboardButton('Отменить участие'),
            KeyboardButton('Запросить перенос времени'),
        ]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    update.message.reply_text("Пользовательское меню", reply_markup=reply_markup)


if __name__ == "__main__":
    load_dotenv()
    bot_token = os.getenv("BOT-TOKEN")

    admins = ["@HardRope"]

    updater = Updater(token=bot_token, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(CommandHandler('admin', admin_button))
    dispatcher.add_handler(CommandHandler('user', user_button))

    updater.start_polling()
