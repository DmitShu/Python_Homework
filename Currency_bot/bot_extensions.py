import requests
import json
from bot_config import cur

class APIException(Exception):
    pass

class Bot_Extensions:
    @staticmethod
    def get_token():

        with open('data\Token') as t:
            return (t.read())

    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise APIException(f'"Введены одинаковые валюты {base} {base}"')

        try:
            quote_ticker = cur[quote]
        except KeyError:
            raise APIException(f'"Не удалось обработать валюту {quote}"')

        try:
            base_ticker = cur[base]
        except KeyError:
            raise APIException(f'"Не удалось обработать валюту {base}"')

        try:
            amount = float(amount)
        except:
            raise APIException(f'"Не удалось обработать количество {amount}"')

        try:
            req = requests.get(f'https://min-api.crypto compare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        except:
            raise APIException(f'"Сервер не отвечает"')

        try:
            total = json.loads(req.content)[cur[base]] * amount
        except:
            raise APIException(f'"Неожиданный ответа сервера: {json.loads(req.content)}"')

        return total
