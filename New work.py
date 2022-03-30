import asyncio

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message

TOKEN = "5258348450:AAGQgtiD0JDD_FmDrxFHtV2u26tzH9tdQ-E"
my_id = 1970625570

loop = asyncio.get_event_loop()
bot = Bot(TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)
async def send_to_admin(dp):
    await bot.send_message(chat_id=my_id, text="Hi  3 I")

@dp.message_handler()
async def echo(message: Message):
    n = f"Salem sen zhazdynba: {message.text}"
    if message.text == "Salem":
        await bot.send_message(chat_id=message.from_user.id, text="Salem. This is Ayat aiogram bot")
    elif message.text == "Years":
        await bot.send_message(chat_id= message.from_user.id, text="18")
    elif message.text == "Golli":
        await bot.send_message(chat_id= message.from_user.id, text="Vashi golli:2, 3, 1")
    elif message.text == "Dom":
        await bot.send_message(chat_id= message.from_user.id, text="Taraz kalasi")
    else:
        await bot.send_message(chat_id=message.from_user.id, text= "otvet zhok")


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=send_to_admin)

