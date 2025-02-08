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


@app.get("/get_actor/{actor_name}")
def read_item(actor_name: str):    
    film = ETL.Films()
    actor = film.get_actor(actor_name) 
    return actor.to_string_actor_info()
    
@app.get("/cantidad_filmaciones_mes/{month}")
def read_item(month: str):    
    film = ETL.Films()
    num_films = film.cantidad_filmaciones_mes(month)
    #print("salimos? con el num de films = ",str(num_films))
    output = str(num_films)+" películas fueron estrenadas en el mes de "+month
    return output

@app.get("/cantidad_filmaciones_dia/{day}")
def read_item(day: str):    
    film = ETL.Films()
    num_films = film.cantidad_filmaciones_dia(day)
    print("salimos? con el num de films = ",str(num_films))
    output = str(num_films)+" películas fueron estrenadas en los dias "+day
    return output

@app.get("/score_titulo/{title}")
def read_item(title: str):    
    film = ETL.Films()
    info_film = film.score_titulo(title)
    print("salimos? con el num de films = ",info_film.to_string())    
    return info_film.to_string()

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

