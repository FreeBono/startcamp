import requests



TOKEN = '1876385821:AAFyAAg-tvFu_KyR8YkN-2RM67fH_i5gfSA'
url = f'https://api.telegram.org/bot{TOKEN}'
    ngrok_url = 'https://6c952a5fb5a7.ngrok.io'
    set_webhook_url = f'{url}/setWebhook?url={ngrok_url}/telegram'

response = requests.get(set_webhook_url)
print(response.text)
