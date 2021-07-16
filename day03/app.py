from flask import Flask, render_template, request
import requests
 TOKEN = '1876385821:AAFyAAg-tvFu_KyR8YkN-2RM67fH_i5gfSA'

    url = f'https://api.telegram.org/bot{TOKEN}'
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/ssafy')
def ssafy():
    return render_template('ssafy.html')


@app.route('/write')
def write():
 return render_template('write.html')

@app.route('/send')
def send():
    #print(request)
    #print(dir(request))
    message = request.args.get('message')
    #print(message)
   
    chat_id = 1832417323
    send_message_url = f'{url}/sendMessage?chat_id={chat_id}&text={message}'
    requests.get(send_message_url)
    return render_template('send.html')

@app.route('/telegram', methods=['post'])
def telegram():
   
response = request.get_json()
    print(response)
    chat_id = response['message']['from']['id']
    text = response['message']['text']
    if text == "누구야?":
        text = "저는 곽동현님의 챗봇입니다."
    send_message_url = f'{url}/sendMessage?chat_id={chat_id}&text={text}'
    requests.get(send_message_url).json()

    return '', 200








if __name__ == '__main__':
    app.run(debug = True)

