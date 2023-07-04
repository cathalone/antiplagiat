import os
import telebot
from pathlib import Path
import application as ap


BOT_TOKEN = '6082801990:AAH6z9B6t8HSiSjA8KSR3FnjdgRDKY4h7Qo'
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    user_name = message.from_user.username

    if not os.path.exists(f"files/{user_name}"):
        os.mkdir(f"files/{user_name}")


    global SAVE_DIR
    SAVE_DIR = f"files/{user_name}"

    global temp_session
    temp_session = []

    bot.reply_to(message, f'Привет! Пришли 2 файла, которые хочешь сравнить')
@bot.message_handler(content_types=['document'])
def handle_file1(message):
    if sum(1 for x in Path(SAVE_DIR).iterdir()) % 2 == 0:
        file1 = message.document
        file1_name = "file1"

        save_path1 = os.path.join(SAVE_DIR, file1_name)
        file1_info = bot.get_file(file1.file_id)
        downloaded_file1 = bot.download_file(file1_info.file_path)

        temp_session.append(save_path1)

        with open(save_path1, 'wb') as new_file:
            new_file.write(downloaded_file1)

    elif sum(1 for x in Path(SAVE_DIR).iterdir()) % 2 == 1:
        file2 = message.document
        file2_name = "file2"

        save_path2 = os.path.join(SAVE_DIR, file2_name)
        file2_info = bot.get_file(file2.file_id)
        downloaded_file2 = bot.download_file(file2_info.file_path)

        temp_session.append(save_path2)

        with open(save_path2, 'wb') as new_file:
            new_file.write(downloaded_file2)

        percentage = ap.pics_gen(temp_session[0], temp_session[1])

        bot.send_media_group(message.chat.id,
                             [telebot.types.InputMediaPhoto(open(photo, 'rb')) for photo in ['pic/pic1.jpg', 'pic/pic2.jpg']])
        bot.send_message(message.chat.id, f"Файлы похожи на {round(percentage*100)} %")

        os.remove(os.path.join(SAVE_DIR, "file1"))
        os.remove(os.path.join(SAVE_DIR, "file2"))

bot.polling()
