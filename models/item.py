from typing import Dict
from bs4 import BeautifulSoup
import re
import requests
import uuid
from common import Database, constants


class Item(object):
    def __init__(self, url: str, tag_name: str, query: Dict, _id: str = None):
        self._url = url
        self._tag_name = tag_name
        self._query = query
        self._price = None
        self._id = _id or uuid.uuid4().hex

    def __repr__(self):
        return f"<Item {self._url}>"

    def load_price(self) -> float:
        response = requests.get(self._url)
        content = response.content
        soup = BeautifulSoup(content, 'html.parser')
        price_string_from_web = soup.find(self._tag_name,  self._query)
        price_string_from_web = price_string_from_web.text.strip()

        pattern = re.compile('(\\d+,?\\d*\\.\\d\\d)')
        """
        + -> one or more of match
        ? -> zero or one of match
        * -> zero or more of match
        """
        match_price = pattern.search(price_string_from_web)
        self._price = float(match_price.group(1))
        return self._price

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "url": self._url,
            "query": self._query,
            "tag_name": self._tag_name
        }

    @staticmethod
    def load_all():
        return Database.find(constants.ITEM_COLLECTION, {})

    def save_to_mongo(self):
        Database.insert(constants.ITEM_COLLECTION, self.json())
