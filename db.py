from datetime import date

from pony.orm import PrimaryKey, Required, Database, Set, Optional, set_sql_debug, desc

db = Database()
db.bind(provider='sqlite', filename='database.sqlite', create_db=True)


def order_by(q, direction, field):
    if not field:
        return q
    if direction == OrderByDirection.asc:
        return q.order_by(lambda f: getattr(f, field))
    return q.order_by(lambda f: desc(getattr(f, field)))


class Person(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    dob = Required(date)
    email = Required(str)
    noc = Required(int)
