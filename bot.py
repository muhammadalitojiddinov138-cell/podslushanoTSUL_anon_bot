import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ContentType
from aiogram.utils import executor

API_TOKEN = os.getenv("API_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(content_types=ContentType.ANY)
async def forward_to_admin(message: types.Message):
    if message.text:
        await bot.send_message(ADMIN_ID, f"Сообщение от анонимного пользователя:\n{message.text}")
    elif message.photo:
        photo = message.photo[-1].file_id
        caption = message.caption if message.caption else "Фото без подписи"
        await bot.send_photo(ADMIN_ID, photo, caption=f"Аноним прислал фото:\n{caption}")
    elif message.document:
        await bot.send_document(ADMIN_ID, message.document.file_id, caption="Аноним прислал документ")
    elif message.voice:
        await bot.send_voice(ADMIN_ID, message.voice.file_id, caption="Аноним прислал голосовое сообщение")
    elif message.video:
        await bot.send_video(ADMIN_ID, message.video.file_id, caption="Аноним прислал видео")
    await message.answer("Сообщение отправлено админу анонимно ✅")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
