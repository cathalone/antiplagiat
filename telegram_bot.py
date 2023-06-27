import os
import telebot

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
BOT_TOKEN = '6082801990:AAH6z9B6t8HSiSjA8KSR3FnjdgRDKY4h7Qo'
# Укажите путь к папке, куда будут сохраняться загруженные файлы
SAVE_DIR = 'C:/Users/di272/PycharmProjects/antiplagiat/files/photos'

bot = telebot.TeleBot(BOT_TOKEN)
file_counter = 0

@bot.message_handler(commands=['start'])
def start(message):
    """Обработчик команды /start."""
    bot.reply_to(message, 'Привет! Пришли мне первый файл, и я загружу его на компьютер лээ.')

@bot.message_handler(content_types=['document'])
def handle_file1(message):
    global file_counter
    if file_counter == 0:
        """Обработчик приема файлов."""
        file1 = message.document
        file1_name = file1.file_name

        save_path1 = os.path.join(SAVE_DIR, file1_name)
        file1_info = bot.get_file(file1.file_id)
        downloaded_file1 = bot.download_file(file1_info.file_path)

        with open(save_path1, 'wb') as new_file:
            new_file.write(downloaded_file1)
        bot.reply_to(message, f'первый файл {file1_name} успешно загружен на компьютер. Скидывай второй, жээс')
        file_counter += 1
    else:
        """Обработчик приема файлов."""
        file2 = message.document
        file2_name = file2.file_name

        save_path2 = os.path.join(SAVE_DIR, file2_name)
        file2_info = bot.get_file(file2.file_id)
        downloaded_file2 = bot.download_file(file2_info.file_path)

        with open(save_path2, 'wb') as new_file:
            new_file.write(downloaded_file2)
        bot.reply_to(message, f'Ураа! Файл {file2_name} успешно загружен на компьютер. Нихуя больше не скидывай')

bot.polling()
