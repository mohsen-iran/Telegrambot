import requests
import time

TOKEN = "7959926951:AAF-pv7Lh8vyQUueRQLofUQx7pTjOd_bQSE"
URL = f'https://api.telegram.org/bot{TOKEN}/'
LAST_UPDATE_ID = None

def get_updates():
    global LAST_UPDATE_ID
    response = requests.get(URL + 'getUpdates', params={'offset': LAST_UPDATE_ID, 'timeout': 10})
    result = response.json()
    if result.get('ok'):
        return result['result']
    return []

def handle_message(message):
    text = message.get('message', {}).get('text', '')
    chat_id = message.get('message', {}).get('chat', {}).get('id')
    if 'سلام' in text:
        send_message(chat_id, 'علیک خوش‌اومدی')

def send_message(chat_id, text):
    requests.post(URL + 'sendMessage', data={'chat_id': chat_id, 'text': text})

def main():
    global LAST_UPDATE_ID
    while True:
        updates = get_updates()
        for update in updates:
            LAST_UPDATE_ID = update['update_id'] + 1
            handle_message(update)
        time.sleep(1)

if __name__ == '__main__':
    main()
