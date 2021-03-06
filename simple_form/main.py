from typing import List

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pony.orm import db_session, select, set_sql_debug

from . import db
from .deps import paginator, Sorter
from .models import Person, Pagination, PersonBase

app = FastAPI()

# CORS middleware for easy testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get("/", response_model=List[Person])
def list_people(pagination: Pagination = Depends(paginator), sort: Sorter = Depends(), search: str = ''):
    with db_session:
        set_sql_debug(True)
        q = select(p for p in db.Person if search in p.name or search in p.email)
        q = db.order_by(q, sort.dir, sort.order_by).page(pagination.page, pagination.size)

        return [p.to_dict() for p in q]


@app.post("/", response_model=Person, status_code=201)
def add_person(person: PersonBase):
    with db_session:
        # Optional duplicate detection
        #  if db.Person.exists(email=person.email):
        #    raise HTTPException(status_code=400, detail="Duplicate")
        return db.Person(**person.dict()).to_dict()
