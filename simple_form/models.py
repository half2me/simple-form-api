from datetime import date

from pydantic import BaseModel, conint, EmailStr, PositiveInt

PageNum = PositiveInt
default_page_size = 30
PageSize = conint(gt=0)


class PersonBase(BaseModel):
    name = str
    dob = date
    email = EmailStr
    noc = conint(ge=0)


class Person(PersonBase):
    id: int


class Pagination(BaseModel):
    page: PageNum = 1
    size: PageSize = default_page_size
