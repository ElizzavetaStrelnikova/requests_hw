import requests
import json
'''the 1st task'''
url = 'https://akabab.github.io/superhero-api/api'
r = requests.get(url+'/all.json', timeout=10)
# print(json.loads(r.content.decode("utf-8")))
all_list = json.loads(r.content.decode("utf-8"))
hero_list = ['Hulk', 'Captain America', 'Thanos']
cleverest = ''
max_iq = 0
for el in all_list:
    if el['name'] in hero_list:
        if el['powerstats']['intelligence'] > max_iq:
            cleverest = el['name']
            max_iq = el['powerstats']['intelligence']
print(cleverest) # Thanos

import requests
import json

'''the 2nd task'''
class YaUploader:
    def init(self, token: str):
        self.token = token
        self.url = 'https://cloud-api.yandex.net:443'

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
        r = requests.get(self.url + '/v1/disk/resources/upload?path=test_upload.txt',
                         headers={'Authorization': f'OAuth {self.token}'}, timeout=10)
        # print(json.loads(r.text))
        upload_link = json.loads(r.text)['href']

        r = requests.put(upload_link, data=open('test.txt', 'rb'))


if name == 'main':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'test.txt'
    token = ''
    uploader = YaUploader(token)
    uploader.upload(path_to_file)