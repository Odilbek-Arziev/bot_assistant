from ..keyboards import *
from ..messages import messages

buttons = {
    'python': '1️⃣ Курс по основам языка Python & Django',
    'javascript': '2️⃣ Курс по основам языка Javascript & React',
    'smm': '3️⃣ Курс по основам СММ-маркетинга',
    'graphic_design': '4️⃣ Курс по основам Графического Дизайна',
    'wordpress': '5️⃣ Курс по основам Wordpress',
    'scratch': '6️⃣ Курс по основам языка Scratch'
}


def start(chat, **kwargs):
    chat.send_message(messages['greeting'], reply_markup=greeting(buttons))


def course_list(chat, callback_data, **kwargs):
    for course in buttons.keys():
        if course == callback_data.get('data'):
            chat.send_message(messages[course], reply_markup=menu())


def ask_first_name(chat, **kwargs):
    chat.send_message('Введите фамилию и имя', reply_markup=cancel_button())


def ask_phone(chat, message, **kwargs):
    chat.last_data = {'name': message.text}
    chat.send_message('Отправьте номер телефона', reply_markup=phone())


def ask_address(chat, message, redirect, **kwargs):
    user_name = chat.last_data.get('name')

    if message.text == '❌ Отмена':
        return redirect(cancel, **kwargs)
    if len(_integers_only(message.text)) != 12:
        return redirect(wrong_phone, **kwargs)

    chat.last_data = {'name': user_name, 'phone': message.text}
    chat.send_message('Выберите регион', reply_markup=regions())


def create_lead(chat, message, **kwargs):
    user_name = chat.last_data.get('name')
    user_phone = chat.last_data.get('phone')

    chat.last_data = {'name': user_name, 'phone': user_phone, 'region': message.text}
    chat.send_message('Спасибо за оставленную заявку. Мы с вами свяжемся в ближайшее время!', reply_markup=final_menu())


def wrong_phone(chat, **kwargs):
    chat.send_message('Номер введен неправильно. Повторите еще раз')


def any_type(chat, **kwargs):
    chat.send_message('Я вас не понимаю')


def cancel(chat, **kwargs):
    chat.last_data = {}
    chat.send_message('Вы отменили заявку', reply_markup=final_menu())


def _integers_only(text) -> str:
    return ''.join(x for x in text if x.isdigit())
