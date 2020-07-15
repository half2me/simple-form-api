from enum import Enum


class OrderByDirection(str, Enum):
    asc = 'asc'
    desc = 'desc'


class OrderByFields(str, Enum):
    name = 'name'
    dob = 'dob'
    email = 'email'
    noc = 'noc'
