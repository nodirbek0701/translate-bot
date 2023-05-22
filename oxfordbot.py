import logging
import requests
from aiogram import Bot,Dispatcher,executor,types
from googletrans import Translator
bot_linki='6132460317:AAG6IS0Gqp01rBT-lWQk7x9bmD5D7SetYS0'

logging.basicConfig(level=logging.INFO)

bot=Bot(token=bot_linki)
dp=Dispatcher(bot)

@dp.message_handler(commands='start')
async def send(message: types.Message):
    await message.reply('Assalomu Alykum va Rahmatullohi va Barakotuh \n Men en/uz tarjimoniman \n menga soz kiriting')
    print(message.chat['first_name'])
@dp.message_handler(commands='help')
async def send_welcome(message: types.Message):
    await message.answer('inglizcha soz kiriting men sizga tarjimasini va talaffuzini chiqarib beraman ')
# @dp.message_handler()
# async def xabarlar(message:types.Message):
#     await bot.send-message(message.chat.id,"salom foydalanuvchi")
#     await bot.send_message(1434052080,f"{message.chat.first_name}\n{message.text}")

@dp.message_handler()
async def oxford(message:types.Message):
    translate_soz=message.text
    tarjimon=Translator()
    uzbekchasi=tarjimon.translate(translate_soz,dest="uz").text
    print(translate_soz)
    tarjima=requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{translate_soz}")
    if tarjima.status_code==200:
        info=tarjima.json()
        await message.reply(f'''{translate_soz} tarjimasi {uzbekchasi}\n
fonetik talaffuzi {info[0]['phonetic']}
UK aytilishi {info[0]['phonetics'][0]['audio']}
USA aytilishi {info[0]['phonetics'][0]['audio']}
Soz turkumi {info[0]['meanings'][0]['partOfSpeech']}''')
        # await bot.send_message(message.chat.id,"salom foydalanuvchi")
        # await bot.send_message(1434052080,f"{message.chat.first_name}\n{message.text}")
        

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)