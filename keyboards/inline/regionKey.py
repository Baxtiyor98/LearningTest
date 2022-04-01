from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# 1 - usul

viloyat = InlineKeyboardMarkup(row_width=2)
viloyat.insert(InlineKeyboardButton(text="Toshkent",callback_data='1_Toshkent'))
viloyat.insert(InlineKeyboardButton(text="Andijon",callback_data='2_Andijon'))
viloyat.insert(InlineKeyboardButton(text="Fargona",callback_data='3_Fargona'))
viloyat.insert(InlineKeyboardButton(text="Namangan",callback_data='4_Namangan'))
viloyat.insert(InlineKeyboardButton(text="Sirdaryo",callback_data='5_Sirdaryo'))
viloyat.insert(InlineKeyboardButton(text="Youtube",url='https://www.youtube.com/'))
viloyat.add(InlineKeyboardButton(text="Keyingi",callback_data='next'))
viloyat.add(InlineKeyboardButton(text="◀️Ortga",callback_data='back'))

# 2 - usul
number = [1,2,3,4,5,6,7,8,9]
sonlar = InlineKeyboardMarkup(row_width=3)
for i in number:
    sonlar.insert(InlineKeyboardButton(text=f"{i}",callback_data=f"_{i}"))
sonlar.add(InlineKeyboardButton(text="◀️Ortga",callback_data='back'))

jins = InlineKeyboardMarkup(row_width=2)
jins.insert(InlineKeyboardButton(text="🙍‍♂️Erkak",callback_data='erkak'))
jins.insert(InlineKeyboardButton(text="👩‍🦰Ayol",callback_data='ayol'))
jins.add(InlineKeyboardButton(text="◀️Ortga",callback_data='back'))

confirm = InlineKeyboardMarkup(row_width=2)
confirm.insert(InlineKeyboardButton(text="✅ Ha",callback_data='1'))
confirm.insert(InlineKeyboardButton(text="❌ Yo'q",callback_data='0'))