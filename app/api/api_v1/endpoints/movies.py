from fastapi import APIRouter
from fastapi.responses import JSONResponse

from ..database import *


# If database is empty - adding 100 items from movies.csv
initiate_db()

router = APIRouter()


@router.get("/")
@router.get("/getmovies")
async def getmovies():
    response = []
    all_movies = get_all_movies()
    print(all_movies)
    response.append(f'Items count {len(all_movies)}')
    for item in all_movies:
        if item:
            resp = {
                'title':item['title']['S'],
                'releaseYear':item['releaseYear']['N'],
                'genre':item['genre']['S'],
                'coverUrl':item['coverUrl']['S']
            }
            response.append(resp)
    return response


@router.get("/getmoviesbyyear/{year}")
async def getMoviesByYear(year):
    response = get_movie_by_year(year)
    return response


@router.get("/getmovie/{name}")
async def getMovies(name):
    response = get_movie_by_name(name.capitalize())
    return response