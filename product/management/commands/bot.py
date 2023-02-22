from django.core.management.base import BaseCommand
from air_nomad import settings
from telebot import types
import telebot
from product.models import Product


bot = telebot.TeleBot(settings.TELEGRAM_BOT_API_KEY, threaded=False)


@bot.message_handler(commands=['start'])
def get_message(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Показать товары aliOP!')
    markup.add(btn1)

    bot.send_message(chat_id, text="Привет, {0.first_name}! Я бот для Air_nomad".format(message.from_user),
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala (message):
    print(message.text)
    chat_id = message.chat.id
    if message.text == 'Показать товары Air_nomand!':
        data = Product.objects.all()
        for dict_ in data:
            bot.send_message(
                chat_id, f"\nTitle: {dict_.title}\n"
                         f"Description: {dict_.description}\n"
                         f"Category: {dict_.category}\n"
                         f"Price: {dict_.price}\n"
                         f"Stock: {dict_.stock}\n"
                         f"Preview: http://127.0.0.1:8000/media/{dict_.preview}\n"
            )
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Новости KaktusMadia')
        markup.add(btn1)
        bot.send_message(chat_id, 'Моя Твоя не понимать.  Введите правильный ID', reply_markup=markup)


class Command(BaseCommand):
    help = 'Implemented to Django application telegram bot setup command'

    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()
        bot.infinity_polling()