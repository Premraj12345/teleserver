import os
import requests
from flask import Flask, send_file
import io

bot_token = os.environ.get('BOT_TOKEN')

app = Flask(__name__)

@app.route('/stream/<file_id>')
def stream_file(file_id):
    url = f"https://api.telegram.org/bot{bot_token}/getFile?file_id={file_id}"
    file_path = requests.get(url).json()['result']['file_path']

    # Construct the direct download link
    download_link = f'https://api.telegram.org/file/bot{bot_token}/{file_path}'

    response = requests.get(download_link)

    return send_file(io.BytesIO(response.content), as_attachment=True,
                         download_name=file_path)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
