from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Nomer ulashish 📞',request_contact=True)
        ],
        [
            KeyboardButton("◀️Ortga")
        ]
    ],
    resize_keyboard=True
)

back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("◀️Ortga")
        ]
    ],
    resize_keyboard=True
)

location = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Lokatsiya',request_location=True)
        ],
        [
            KeyboardButton(text='Link'),
            KeyboardButton("◀️Ortga")
        ],
    ],
    resize_keyboard=True
)

def bolim():
    return ReplyKeyboardMarkup(
        keyboard = [
                       [
                           KeyboardButton('1'),
                           KeyboardButton('2'),
                           KeyboardButton('2.1')
                       ],
                       [
                           KeyboardButton('3'),
                           KeyboardButton('3.1')
                       ],
                       [
                           KeyboardButton('4')
                       ],
                   ],
        resize_keyboard = True
        )
