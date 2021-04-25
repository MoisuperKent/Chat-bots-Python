import telebot #Используем модуль готовой библиотеки нашего бота
import emoji #Подключаем модуль, позволяющий нашему боту использовать эмоджи (смайлики)
import random #Подключаем модуль, который нам нужен для генерации случайного ответа
import os
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types
bot=telebot.TeleBot("1789983225:AAFCdTjxAaUG2REU1wUfZerwjg5SXITzjk8") #Подключаем нашего бота, используя его токен
# Заготавливаем стикеры
stick=["CAACAgIAAxkBAAECIGJgY3quAAHNwSx-kp-Itu5QwW0VZ-YAAhIAAztkrz-OniNONGBtRB4E", "CAACAgIAAxkBAAECIGBgY3pmVQABS-FJfZzkNdlZDAqmIF0AArYAAxAP3jLMmPRAZvrPpR4E", "CAACAgIAAxkBAAECIF5gY3oFGaCkAhD7cGq9gYkS26BYhQAChQIAAladvQqjCXIQX5cmGR4E",\
"CAACAgIAAxkBAAECIGRgY33bxFHxlnejYP2sJEe0oVoR0gACVAADDnr7CkTSKLrjuRnPHgQ", "CAACAgIAAxkBAAECIGZgY34hR4arZxyDDBpeoLHl2J7BegACOwMAArrAlQW_-vJKNQ1vvh4E", "CAACAgIAAxkBAAECIGhgY34o2KnHmlvUcFRnphJd-9JpNQACHQADO3EfIqmCmmAwV9EZHgQ", "CAACAgIAAxkBAAECIGpgY35Od76g5CH4W9xRfNVGFfYHUAACZgAD8NhFFqkcWfaaIN9eHgQ",\
"CAACAgEAAxkBAAECIGxgY35WDQFQxh24LKLMv449DweJsAACZAoAAr-MkAQygG78Al4ctR4E",  "CAACAgEAAxkBAAECIG5gY35YUpAmQtwgZPNCJsmGljdl2QACZgoAAr-MkASwNJ0LbWtF4h4E", "CAACAgIAAxkBAAECIHBgY35wqMKK9lYJtC133EAw-x82DgAC6AIAAladvQq8XxuFroIfJx4E", "CAACAgIAAxkBAAECIHJgY359yTwHc7peOSuQeSgdubCWUQACtQUAAj-VzAreKic7gwuwih4E",\
"CAACAgIAAxkBAAECIHRgY361HbKUQLgIc1QYXJVbKEzNrAACkgIAAladvQp7nZp4DMOYdx4E", "CAACAgIAAxkBAAECIHZgY37H6kK6kIraKguehLizfB6f9gACZwMAAvPjvgsoZEPKbYNt8B4E", "CAACAgIAAxkBAAECIHhgY37z_cwV68-28pJxg5srBQ4GPwACdwADr8ZRGjPYo3l-8_KyHgQ",\
"CAACAgIAAxkBAAECIHpgY38Hbi22d1bxEUbY1biVCu1FHgACOwEAAooSqg5WysIGqZgJaB4E", "CAACAgIAAxkBAAECIHxgY3-gGz8TE8T8tbJnz7BFotMLEQACDgADO2SvP6uGvCZ5at4wHgQ", "CAACAgIAAxkBAAECIH5gY3-vVZoTM-bUJPGeXcdXtZ6CegACCwADO2SvP_hphHmTBxzRHgQ",\
"CAACAgIAAxkBAAECIIBgY3-06j_2cXFsa1usfFYX9gb44wACEwADO2SvP8olSSwzZI1vHgQ",  "CAACAgIAAxkBAAECIIJgY3-5gTyPGSj-pNac4OXRDCjy6wACAgEAAsGRsiT9mPX4hHsTMh4E", "CAACAgEAAxkBAAECIIRgY3_NyWQvsOF2XW-8VpbkUJzDGwACewoAAr-MkARDATXnuS7ZNh4E",\
"CAACAgEAAxkBAAECIIZgY3_Yt_TDGTV8p-hr_QPBezjPiQACCgAD-MARTpXd3tItLErrHgQ",  "CAACAgIAAxkBAAECIIhgY3_n1z6yfHhJb3hyvg6p9OVUZwACUwIAAladvQq9xYpEKcd7Qx4E", "CAACAgIAAxkBAAECIIpgY4AC7mi0LkjgpsQFAuodW_r0ZwACewADHwFMFexzG_osDiJZHgQ"]
# Заготавливаем комплименты
compliments=["Сколько лет живу, но лучше вас никого не встречал "+emoji.emojize(":star:", use_aliases=True), "Вы красивы, как алая роза "+emoji.emojize(":rose:", use_aliases=True), "Мне нравится ваш лук (одежда) "+emoji.emojize(":thumbs_up:", use_aliases=True),\
"Вы прекрасны, как первая заря "+emoji.emojize(":sunrise:", use_aliases=True), "Вы способны затмить своим видом солнце "+emoji.emojize(":sunglasses:", use_aliases=True), "Смотря на вас, ко мне поступают только положительные запросы "+emoji.emojize(":alien_monster:", use_aliases=True),\
"Ой, кажется мне нужен спасатель-я тону в ваших глазах "+emoji.emojize(":hollow_red_circle:", use_aliases=True), "Ваш взгляд греет меня сильней, чем процессор в телефоне моего создателя греется от новинок видеоигр "+emoji.emojize(":fire:", use_aliases=True),\
"Будь я ботом, делающим арты, то писал бы их с вас "+emoji.emojize(":artist:", use_aliases=True)]
# Кнопка с рекламой
keyboard = types.InlineKeyboardMarkup()
url_button = types.InlineKeyboardButton(text="Перейти", url="https://t.me/Oracle_of_GodsBot")
keyboard.add(url_button)
#  (горячие кнопки)
choice = telebot.types.ReplyKeyboardMarkup(True).add("Вдохновляющая цитата "+emoji.emojize(":thought_balloon:", use_aliases=True)).add("Комплимент "+emoji.emojize(":love_letter:", use_aliases=True)).add("Побудить к действиям "+emoji.emojize(":hiking_boot:", use_aliases=True))
@bot.message_handler(commands=['start'])
def start_message(message):
    welcome=open("Greeting/welcome.jpg", 'rb')
    bot.send_photo(message.from_user.id, welcome, caption = 'Каждому время от времени нужно вдохновление, заряд позитивных эмоций или небольшое давление. И раз уж вы сегодня обратились ко мне, я готов вам их предоставить.', reply_markup=choice)
    bot.send_message(message.chat.id, "Пользуясь случаем, хочу посоветовать также моего собрата, который также, как и я, был создан моим создателем"+"\n(не реклама "+emoji.emojize(":smiling_face_with_halo:", use_aliases=True)+")", reply_markup=keyboard) 
# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(commands=['help'])
def get_help(message):
     bot.send_message(message.chat.id, "Чтобы воспользоваться мной, используйте кнопки ниже"+emoji.emojize(":backhand_index_pointing_down:", use_aliases=True))
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == "вдохновляющая цитата" or message.text == "Вдохновляющая цитата "+emoji.emojize(":thought_balloon:", use_aliases=True):
        photo = open('images/' + random.choice(os.listdir('images')), 'rb')
        bot.send_photo(message.from_user.id, photo, caption = 'По вашему заказу')
    elif message.text.lower() == 'побудить к действиям' or message.text =="Побудить к действиям "+emoji.emojize(":hiking_boot:", use_aliases=True):
        video = open('Labaf/'+ random.choice(os.listdir('Labaf')), 'rb')
        bot.send_message(message.chat.id, text='Пожалуйста, подождите немного, видео обрабатывается...'+emoji.emojize(":optical_disk:", use_aliases=True))
        bot.send_video(message.chat.id, video, caption = 'Приготовьтесь к заряду мотивации на целый день, так как это видео точно побудит вас встать с дивана')
    elif message.text.lower() == 'комплимент' or message.text == "Комплимент "+emoji.emojize(":love_letter:", use_aliases=True):
        compliment=random.choice(compliments)
        bot.send_message(message.chat.id, compliment)
    else: bot.send_message(message.chat.id, "Кажется вы хотите поболтать, угадал? Но, к сожалению, мой создатель не разрешает мне разговаривать с людьми, потому что боиться, что я скажу что-нибудь не то..."+emoji.emojize(":pensive_face:", use_aliases=True))
@bot.message_handler(content_types=['sticker'])
def get_text_messages(message):
    s=random.choice(stick)
    bot.send_message(message.chat.id, "О, я тоже так умею!!! "+emoji.emojize(":smiling_face_with_sunglasses:", use_aliases=True)+ "\n" +"Смари..."+emoji.emojize(":face_savoring_food:", use_aliases=True)) 
    bot.send_sticker(message.chat.id, s)
@bot.message_handler(content_types=['video'])
def get_video(message):
    bot.send_message(message.chat.id, "Кажется вы отправили мне видео, да? Я сейчас немного занят, но обязательно посмотрю его позже, как только у меня появиться свободное время..."+emoji.emojize(":grinning_face_with_sweat:", use_aliases=True))
@bot.message_handler(content_types=['audio'])
def get_audio(message):
    bot.send_message(message.chat.id, "Качает трек, пора навести суету "+emoji.emojize(":smiling_face_with_sunglasses:", use_aliases=True)+emoji.emojize(":call_me_hand:", use_aliases=True))
@bot.message_handler(content_types=['voice'])
def get_voice(message):
    bot.send_message(message.chat.id, "Какой приятный голос "+emoji.emojize(":smiling_cat_with_heart-eyes:", use_aliases=True)+"\n"+"Вам бы исполнять хиты, возможно попали бы в топ чарты... "+emoji.emojize(":backhand_index_pointing_right:", use_aliases=True) +emoji.emojize(":backhand_index_pointing_left:", use_aliases=True))
    bot.send_message(message.chat.id, "Вот, возьмите мой микрофон и сходите в караоке "+emoji.emojize(":microphone:", use_aliases=True))
@bot.message_handler(content_types=['document'])
def get_doc(message):
    bot.send_message(message.chat.id, "Создатель говорит: ''Нельзя принимать файлы от малознакомых людей'' "+emoji.emojize(":index_pointing_up:", use_aliases=True))
@bot.message_handler(content_types=['contact'])
def get_cont(message):
    bot.send_message(message.chat.id, "Это кто? (Who?) "+emoji.emojize(":face_with_raised_eyebrow:", use_aliases=True))
@bot.message_handler(content_types=['poll'])
def get_vote(message):
    bot.send_message(message.chat.id, "О, опрос, люблю опросы... "+emoji.emojize(":face_savoring_food:", use_aliases=True))
    audio=open('audio/Включи.mp3','rb')
    bot.send_audio(message.chat.id, audio)
@bot.message_handler(content_types=['location'])
def get_loc(message):
    bot.send_message(message.chat.id, "Классно, а я навечно заперт в вашем девайсе... "+emoji.emojize(":smiling_face_with_tear:", use_aliases=True))
@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.send_message(message.chat.id, "Классное фото "+emoji.emojize(":OK_hand:", use_aliases=True))
# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)

    
