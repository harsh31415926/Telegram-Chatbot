import logging
from aiogram import Bot , Dispatcher , types 
import asyncio
from dotenv import load_dotenv
import os
from aiogram.filters import Command # Line 29


load_dotenv()

bot_token = os.getenv("TELEGRAM_BOT_TOKEN")

logging.basicConfig(level =logging.INFO) # Tells the level of message [ debug < info < warning < error < critical ]

bot = Bot(token = bot_token)

dp = Dispatcher()

@dp.message(Command(commands=['start', 'help', 'info']))
async def command_start_handler(message: types.Message):
    """
    Handles the command of the user
    """

    await message.reply("Hello! I am a servant of Shree Shree 1008 Harsh Sharma ji ji sir sir")



@dp.message() # Dispatcher we have to give to activate 
async def echo(message : types.Message):

    """
    This just echoes the message
    """

    await message.answer(message.text)

async def main():
    await dp.start_polling(bot , skip_updates = True) 

if __name__ == "__main__":
    asyncio.run(main())