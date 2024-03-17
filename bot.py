import random
import string
from telegram import Update, BotCommand
from telegram.ext import Application, CommandHandler, CallbackContext

def generate_password(length=12, use_special_chars=True):
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        'Привет! Я Passix, твой помощник для генерации паролей.\n'
        'Используй /simple для простого пароля или /complex для сложного пароля.')

async def simple_password(update: Update, context: CallbackContext) -> None:
    password = generate_password(length=8, use_special_chars=False)
    await update.message.reply_text('Ваш простой пароль:')
    await update.message.reply_text(password)

async def complex_password(update: Update, context: CallbackContext) -> None:
    password = generate_password(length=12, use_special_chars=True)
    await update.message.reply_text('Ваш сложный пароль:')
    await update.message.reply_text(password)

def main() -> None:
    application = Application.builder().token('6783229255:AAH5gzwoNoXLXW9akWACOPy9m3IzpeynWTw').build()

    # Добавление команд для удобства пользователя
    application.bot.set_my_commands([
        BotCommand("simple", "Сгенерировать простой пароль"),
        BotCommand("complex", "Сгенерировать сложный пароль")
    ])

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("simple", simple_password))
    application.add_handler(CommandHandler("complex", complex_password))

    application.run_polling()

if __name__ == '__main__':
    main()
