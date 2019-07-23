import requests
from config import config


def send_message(email, phone, text):
    message = 'Вам пришел отзыв: \n' \
              'email: ' + email + '\n' \
                                  'phone: ' + phone + '\n' \
                                                      'text: ' + text
    token = config.token
    method = 'sendMessage'
    response = requests.post(
        url='https://api.telegram.org/bot{0}/{1}'.format(token, method),
        data={'chat_id': 248329110, 'text': message}
    ).json()
    return response
