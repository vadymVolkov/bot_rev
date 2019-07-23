

import telebot


class Keyboard:
    def __init__(self, bot):
        self.bot = bot

    def test(self, message):
        user_id = message.from_user.id
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('/start', '/reg')
        self.bot.send_message(user_id, 'hi your user id is ' + str(user_id), reply_markup=user_markup)
