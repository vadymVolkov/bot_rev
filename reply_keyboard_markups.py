import telebot


class Keyboard:
    def __init__(self, bot):
        self.bot = bot

    def start(self, message):
        user_id = message.from_user.id
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('/start', '/reg')
        self.bot.send_message(user_id,
                              'Привет! Я бот который будет присылать тебе отзывы! Если те еще не зарегестрировался, запусти команду /reg !',
                              reply_markup=user_markup)
