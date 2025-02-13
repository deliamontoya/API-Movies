from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
import import_ipynb
import ETL 
import Recomendation

app = FastAPI()


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

@app.get("/votos_titulo/{title}")
def read_item(title: str):    
    film = ETL.Films()
    info_film = film.votos_titulo(title)

    print("salimos? con el num de films = ",info_film.to_string_votos_titulo())    
    return info_film.to_string_votos_titulo()

@app.get("/get_director/{director_name}")
def read_item(director_name: str):    
    film = ETL.Films()
    director = film.get_director(director_name) 
    return director.to_string_info_director()

@app.get("/get_recommendations_by_title/{title}")
def read_item(title: str):    
    print("hola para la recomendaion")
    rec = Recomendation.Recomention()
    titles = rec.get_recommendations_by_title(title)
    print("titles: ",titles)
    return str(titles)

@app.get("/get_recommendations_by_weight/{title}")
def read_item(title: str):    
    print("hola para la recomendaion: get_recommendations_by_weight")
    rec = Recomendation.Recomention()
    titles = rec.get_recommendations_by_weigh(title)
    print("titles: ",titles)
    return str(titles)

@app.get("/get_recommendations_by_words/{title}")
def read_item(title: str):    
    print("hola para la recomendaion: get_recommendations_by_words")
    rec = Recomendation.Recomention()
    titles = rec.get_recommendations_by_words(title)
    print("titles: ",titles)
    return str(titles)