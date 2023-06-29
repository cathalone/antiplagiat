import os
import telebot
from pathlib import Path

BOT_TOKEN = '6082801990:AAH6z9B6t8HSiSjA8KSR3FnjdgRDKY4h7Qo'
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    #узнаем тег пользователя
    user_name = message.from_user.username

    #если не существует папки с таким же именем, как и тег пользователя, то создаем ее
    if not os.path.exists(f"C:/Users/di272/PycharmProjects/antiplagiat/files/{user_name}"):
        os.mkdir(f"C:/Users/di272/PycharmProjects/antiplagiat/files/{user_name}")

    global SAVE_DIR
    SAVE_DIR = f"C:/Users/di272/PycharmProjects/antiplagiat/files/{user_name}"


    bot.reply_to(message, f'Привет! Пришли мне первый файл, и я загружу его на компьютер в папку {SAVE_DIR} лээ.')

@bot.message_handler(content_types=['document'])
def handle_file1(message):

    #когда мы получаем первый файл, то мы сразу отправляем его в текущий лист ожидания (до того момента, пока не получим пару к этому файлу)
    #example: temp list = [file1,...]
    if sum(1 for x in Path(SAVE_DIR).iterdir()) % 2 == 0:
        file1 = message.document
        file1_name = file1.file_name

        save_path1 = os.path.join(SAVE_DIR, file1_name)

        file1_info = bot.get_file(file1.file_id)
        downloaded_file1 = bot.download_file(file1_info.file_path)

        with open(save_path1, 'wb') as new_file:
            new_file.write(downloaded_file1)
        bot.reply_to(message, f'первый файл {file1_name} успешно загружен на компьютер. Скидывай второй, жээс')

    #на этом этапе у нас есть 2 файла: первый файл и файл, с которым мы хотим сравнить наш первый файл
    elif sum(1 for x in Path(SAVE_DIR).iterdir()) % 2 == 1:
        file2 = message.document
        file2_name = file2.file_name

        save_path2 = os.path.join(SAVE_DIR, file2_name)
        file2_info = bot.get_file(file2.file_id)
        downloaded_file2 = bot.download_file(file2_info.file_path)

        with open(save_path2, 'wb') as new_file:
            new_file.write(downloaded_file2)
        bot.reply_to(message, f'Ураа! Файл {file2_name} успешно загружен на компьютер. Нихуя больше не скидывай')

bot.polling()
