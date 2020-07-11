from flask import Flask
from models import Item

#
# app = Flask(__name__)
#
# if __name__ == "__main__":
#     app.run()


URL = "https://www.johnlewis.com/lego-star-wars-75192-ultimate-collector-series-millennium-falcon/p3410616"
tag = "p"
query = {"class": "price price--large"}

item = Item(URL, tag, query)
print(item.load_price())
