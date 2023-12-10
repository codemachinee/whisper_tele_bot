import whisper
from aiogram import Bot, Dispatcher, F
import asyncio
import os
from paswords import *
token = codemashine_test
bot = Bot(token=token)
dp = Dispatcher()


@dp.message(F.voice, F.chat.type == 'private')
async def chek_message(v):
    await save_audio(bot, v)


async def save_audio(bot, message):
    await bot.send_message(message.chat.id, f'есть контакт')
    file_id = message.voice.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    await bot.download_file(file_path, f"{file_id}")
    model = whisper.load_model("medium")
    result = model.transcribe(f"{file_id}")
    await bot.send_message(message.chat.id, f'{result["text"]}')
    os.remove(f"{file_id}")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')