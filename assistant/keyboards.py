from botmother.utils.keyboards import *


def greeting(array):
    return inline_keyboard([
        [inline(value, {'data': key}, 'is-course')] for key, value in array.items()
    ])


def regions():
    return keyboard([
        [button('г.Бухара'), button('Бухара регион')],
        [button('Каган'), button('Вапкент')],
        [button('Жондор'), button('Ромитан')],
        [button('Олот'), button('Пешку')],
        [button('Каракуль'), button('Караул Базар')],
        [button('Гиждуван'), button('Шофиркон')],
        [button('❌ Отмена')]
    ])


def menu():
    return inline_keyboard([
        [inline('📩 Оставить заявку', {'value': 'leave_lead'}, 'is-lead')],
        [inline('◀️ Назад', {'value': 'back'}, 'is-back')]
    ])


def phone():
    return keyboard([
        [button('Поделится контактом', contact=True)],
        [button('❌ Отмена')]
    ])


def cancel_button():
    return keyboard([
        [button('❌ Отмена')]
    ])


def final_menu():
    return keyboard([
        [button('📋 Посмотреть список курсов')]
    ])
