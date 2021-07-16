import requests
#from pprint import pprint
TOKEN = '1876385821:AAFyAAg-tvFu_KyR8YkN-2RM67fH_i5gfSA'

url = f'https://api.telegram.org/bot{TOKEN}/'
print(url)

get_updates_url = f'{url}getUpdates'
print(get_updates_url)
response = requests.get(get_updates_url).json()
#pprint(response)
chat_id = response['result'][0]['message']['from']['id']
text = response['result'][0]['message']['text']
print(chat_id,text)


send_message_url = f'{url}/sendMessage?chat_id={chat_id}&text={text}'
requests.get(send_message_url).json()