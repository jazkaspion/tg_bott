import ast

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup

from services import *

try:
    create_table_log()
    creat_table()
except Exception as e:
    pass
bts = [
    [KeyboardButton("🥇 QASHQADARYO")],
    [KeyboardButton("TOSHKENT"), KeyboardButton("SURXANDARYO")],
    [KeyboardButton("FARG`ONA"), KeyboardButton("ANDIJON"), KeyboardButton("NAMAHGAN")],
    [KeyboardButton("NAVOIY"), KeyboardButton("XORAZIM"), KeyboardButton("JIZZAX"), KeyboardButton("BUXORO")],
    [KeyboardButton("QORAQALPOG`ISTON")]
]
contact = [
    [KeyboardButton("contact", request_contact=True)]

]


def to_dict(strr):
    print(strr, type(strr))
    return ast.literal_eval(strr)




def start(update, context):
    user = update.message.from_user
    try:
        create_user_Log(user_id=user.id)
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaa")
        create_user(user_id=user.id, username=user.username)
        print("kemadi")
    except Exception as e:
        print("xatolik: ", e)
    clear_state(user_id=user.id)
    print("plk")
    log = to_dict(get_user_Log(user.id)[0])
    print("QWER")
    if log["state"] == 10:
        update.message.reply_text("siz ro`yxatdandingiz")
    else:
        log['state'] = 1
        print("log: ", log)
        change_Log(message=log, user_id=user.id)
        print("qwer")
        update.message.reply_text("Assalomu alaykum ismingizni kiriting")


def recived_message(update, context):
    msg = update.message.text
    user = update.message.from_user
    log = to_dict(get_user_Log(user.id)[0])
    log['state'] = 1

    if log.get('state', 0) == 1:
        log['isim'] = msg
        log['state'] = 2
        update.message.reply_text("famelyangizni kiriting")
    elif log.get('state', 0) == 2:
        log['familiya'] = msg
        log['state'] = 3
        update.message.reply_text("viloyatingizni tanlang",
                                  reply_markab=ReplyKeyboardMarkup(bts, resize_keyboard=True))
    elif log.get('state', 0) == 3:
        log['viloyati'] = msg
        log['state'] = 4
        update.message.reply_text("raqamingizni kiriting",
                                  reply_markab=ReplyKeyboardMarkup(contact, resize_keyboard=True))

    change_Log(user.id, log)


def recived_contact(update, context):
    contact = update.message.contact
    user = update.message.from_user
    log = to_dict(get_user_Log(user.id)[0])
    if log['state'] == 4:
        log['phone'] = contact.phone_number
        edit_user(log, user.id)
        change_Log(message={"state": 10}, user_id=user.id)
        update.message.reply_text('malumotlar uchun raxmat')


def main():
    TOKEN = "2122989991:AAGjoIFXYTsIm2Y5aK5X1wu8zOGKDb0ZZH4"
    updater = Updater(TOKEN)

    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, recived_message))
    updater.dispatcher.add_handler(MessageHandler(Filters.contact, recived_contact))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
