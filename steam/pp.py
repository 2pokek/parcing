import requests
from bs4 import BeautifulSoup

url = 'https://store.steampowered.com/app/227300/Euro_Truck_Simulator_2/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

game = soup.find('div',classmethod='game_area_purchase_game').text
price

TOKEN_INFO = '5608674607:AAGa6zz-MJhN7MRvpVKWlMRVY8JRiZr9_Kw'
id_chat = ''
message_is = 'Games price is - ' + str(price) + '\n' + url
requests.get('t.me/Steam_priceseses_bot/'.format(TOKEN_INFO),
             params=dict(chat_id=id_chat,text=message_is))