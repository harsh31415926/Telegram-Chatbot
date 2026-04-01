from aiogram import Bot, Dispatcher, types
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import os
import asyncio
from dotenv import load_dotenv
from aiogram.filters import Command

load_dotenv()

groq_api = os.getenv("GROQ_API_KEY")
token = os.getenv("TELEGRAM_BOT_TOKEN")

bot = Bot(token=token)
dispatcher = Dispatcher()

# Conversation history
conversation_history = [
    SystemMessage(content="You are a helpful AI assistant named HarshBot. Answer the user's questions clearly and concisely. Never repeat or echo what the user said.")
]

llm_client = ChatGroq(        # ← renamed to llm_client
    model='llama-3.3-70b-versatile',
    api_key=groq_api
)

def clear_past():
    conversation_history.clear()


@dispatcher.message(Command(commands=['clear']))
async def clear_response(message: types.Message):
    clear_past()
    await message.reply("Cleared History")


@dispatcher.message(Command(commands=['info']))
async def info(message: types.Message):
    await message.reply("This bot is created by your nicest person in this world\nGuess who??\nYes, it is the legend the myth the most bodacious man on this planet\nNone other than\nMr.Harsh Sharma")


@dispatcher.message(Command(commands=['start']))
async def start(message: types.Message):
    await message.reply("Thanks for starting this bot, this is the best LLM based bot you will ever see\nDon't you dare go anywhere else\nLove you guys by your loving Harsh Sharma")


@dispatcher.message(Command(commands = ['personal']))
async def personal(message:types.Message):
    await message.reply("This bot will be shared to some special people of mine \nIt might include my family , friends or some aquintances \nBTW you know one thing \nthis sh#t ain't over yet ")
    

@dispatcher.message(Command(commands=['help']))
async def helper(message: types.Message):
    help_cmd = """This is the bot created by Harsh Sharma
    /start -> start the bot
    /info -> Give the information about the bot
    /clear -> clear chat history
    /personal -> some personal sh$t
    I hope this helped ...... :)
    """
    await message.reply(help_cmd)


@dispatcher.message()           # ← added ()
async def chat(message: types.Message):     # ← renamed to chat
    """
    This will handle all the task related to anything
    """
    print(f"User >>>> \t {message.text}")

    conversation_history.append(HumanMessage(content=message.text))

    response = llm_client.invoke(conversation_history)

    conversation_history.append(AIMessage(content=response.content))

    print(f"LLM >>>> \t {response.content}")

    await bot.send_message(chat_id=message.chat.id, text=response.content)


async def main():
    await dispatcher.start_polling(bot, skip_updates=False)


if __name__ == "__main__":
    asyncio.run(main())