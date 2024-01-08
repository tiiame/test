from aiogram import Bot, Dispatcher, executor, types
from integrations import get_weather_data

bot = Bot("6355962593:AAH-Uv5SF_3kobYqIWxm23Tcy8M8VvcS7JU")
dp = Dispatcher(bot)


async def on_startup(_):
    print("Bot ishga tushdi")

async def is_subscribed(user_id):
    chat_id = "@https://t.me/suxalii_bot"
    try:
        member = await bot.get_chat_member(chat_id, int(user_id))
        if member.status == types.ChatMemberStatus.MEMBER or member.status == types.ChatMemberStatus.CREATOR:
            return True
    except Exception as e:
        print(e)
        return False



@dp.message_handler(commands=['start'])
async def start_btn(message: types.Message):
    if await is_subscribed(message.chat.id):
        return await message.answer(text="Ob-havo botimizga hush kelibsiz, shahar nomini kiriting")
    await message.answer(text="Botimizga xozircha kira olmaysiz")


@dp.message_handler()
async def weather_city(message: types.Message):
    city = message.text
    text = get_weather_data(city)
    await message.answer(text)



if __name__ == "main":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)