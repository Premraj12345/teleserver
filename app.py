import os
from telethon.sync import TelegramClient
from flask import Flask, send_file

api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
bot_token = os.environ.get('BOT_TOKEN')

app = Flask(__name__)

@app.route('/stream/<file_id>')
def stream_file(file_id):
    with TelegramClient('anon', api_id, api_hash) as client:
        message = client.get_messages('@your_channel_username', ids=int(file_id))
        file_path = client.download_media(message.media, file='./downloads/')
        return send_file(file_path)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
