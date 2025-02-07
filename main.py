from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
import import_ipynb
import ETL 

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None




@app.get("/")
def read_root():
    return {"API": "Movies"}


@app.get("/actor/{actor_name}")
def read_item(actor_name: str, q: Union[str, None] = None):    
    film = ETL.Films()
    no_films = film.get_actor(actor_name)
    print("El número de filmaciones son: ", no_films)
    return {"item_id": actor_name, "no_films": no_films}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

