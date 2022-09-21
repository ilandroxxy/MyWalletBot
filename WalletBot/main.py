import telebot
from telebot import types
import datetime as dt

# 👉 🙏 👆 👇 😅 👋 🙌 ☺️ ❗ ️‼️ ✌️ 👌 ✊ 👨‍💻  🤖 😉  ☝️ ❤️ 💪 ✍️ 🎯  ` ⛔  ️✅ 📊📈🧮
bot = telebot.TeleBot('5575461083:AAFUmb4VUvxf2KTFStiagWVGbGzoU-WOv2A')
# real 5575461083:AAFUmb4VUvxf2KTFStiagWVGbGzoU-WOv2A
# test 5734914555:AAEPdNUsCpv4n49jie8C9P7TojK_McPkCIU

Result = []
Summ = []


# START
@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.id == 1891281816 or message.chat.id == 438879394:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Доход ✅')
        btn2 = types.KeyboardButton('Расход ⛔')
        btn3 = types.KeyboardButton('История расходов')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, 'Простой учет доходов 📊📈🧮', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Извините, у вас нет прав доступа 👨‍💻")

'''
@bot.message_handler(commands=['new'])
def new(message):
    bot.send_message(message.chat.id, "🤖 Отправьте мне текст, я его скушаю и заведу в систему\n\n*Напишите `0`, чтобы отменить команду!*")

    @bot.message_handler(content_types=['text'])
    def message_input(message):
        if message.text != '0':
            M = [i for i in message.text.split('\n')]

            for i in range(0, len(M)):
                Result.append(i)
            print(Result)
            bot.send_message(message.chat.id, f"Общая сумма счета на данный момент:\n"
                                              f"*равна {sum(Summ)} рублей*", parse_mode='Markdown')

    bot.register_next_step_handler(message, message_input)
'''





@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip()

    if get_message_bot == 'Доход ✅':
        now = dt.datetime.utcnow()
        nsk_now = now + dt.timedelta(hours=7)
        timer = nsk_now.strftime('%d #%b%Y ')

        bot.send_message(message.chat.id, "[+price] [comment]\n\n*Напишите `0`, чтобы отменить команду!*")
        @bot.message_handler(content_types=['text'])
        def message_input(message):
            if message.text != '0':
                M = [i for i in message.text.split()]
                Summ.append(int(M[0]))
                Result.append(timer + '  +' + message.text)

                bot.send_message(message.chat.id, f"Общая сумма счета на момент:\n"
                                                  f"[{timer}] *равна {sum(Summ)} рублей*", parse_mode='Markdown')
        bot.register_next_step_handler(message, message_input)

    if get_message_bot == 'Расход ⛔':
        now = dt.datetime.utcnow()
        nsk_now = now + dt.timedelta(hours=7)
        timer = nsk_now.strftime('%d #%b%Y ')

        bot.send_message(message.chat.id, "[+price] [comment]\n\n*Напишите `0`, чтобы отменить команду!*")

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            if message.text != '0':
                M = [i for i in message.text.split()]
                Summ.append(-int(M[0]))
                Result.append(timer + '  -' + message.text)

                bot.send_message(message.chat.id, f"Общая сумма счета на момент:\n"
                                                  f"[{timer}] *равна {sum(Summ)} рублей*", parse_mode='Markdown')

        bot.register_next_step_handler(message, message_input)

    if get_message_bot == 'История расходов':
        message_text = "\n".join(Result)
        bot.send_message(message.chat.id, message_text)


bot.polling(none_stop=True)