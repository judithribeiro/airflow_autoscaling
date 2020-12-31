from airflow.models import Variable
import requests
import json
from abc import ABC, abstractclassmethod
import math


class ApiNetimovelAbstract(ABC):
    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        self._pages = value

    @abstractclassmethod
    def get_records(self, id: str) -> json: pass


class ApiNetimovel(ApiNetimovelAbstract):
    def __init__(self):
        print("ApiNetimovel")

    def get_records(self) -> json:
        url = f"{Variable.get('API_NETIMOVEIS_URL')}&pagina={self.page}"
        payload = {}
        headers = self.__get_headers()
        response = requests.request("GET", url, headers=headers, data=payload)
        records = response.text.encode('utf8')
        records = json.loads(records)
        print(records["totalDeRegistros"])
        total = records["totalDeRegistros"]
        self.pages = math.ceil(total / 42)
        return records

    def __get_headers(self):
        return {
                  'authority': 'www.netimoveis.com',
                  'accept': 'application/json, text/javascript, */*; q=0.01',
                  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
                  'x-requested-with': 'XMLHttpRequest',
                  'sec-fetch-site': 'same-origin',
                  'sec-fetch-mode': 'cors',
                  'sec-fetch-dest': 'empty',
                  'referer': 'https://www.netimoveis.com/venda/minas-gerais/belo-horizonte?transacao=venda&localizacao=BR-MG-belo-horizonte---&pagina=1',
                  'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                  'cookie': '__cfduid=d9c91b23ba2b164fe54b71dd3554a882f1606949697; _fbp=fb.1.1606949709189.80306282; _ga=GA1.2.1398145170.1606949709; rl_visitor_history=2c5c03f3-90a8-4c9c-8639-f4e175132914; cookie_guidid=1f36aefd-baf9-4d2d-abd1-03b95c0c0db9; _vstidss_=28a163a3-bf1c-4737-b385-20e1a6356e9e; _gid=GA1.2.1821823546.1607554181'
                }


class ApiNetiovelFactory:
    @staticmethod
    def get_api() -> ApiNetimovelAbstract:
        return ApiNetimovel()


# if __name__ == '__main__':
#     api = ApiNetiovelFactory.get_api()
#     api.page = 1
#     records = api.get_records()
#     print(records)




