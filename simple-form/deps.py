from .enums import OrderByDirection, OrderByFields
from .models import PageNum, PageSize, Pagination, default_page_size


def paginator(page: PageNum = 1, size: PageSize = default_page_size):
    return Pagination(page=page, size=size)


class Sorter:
    def __init__(self, order_by: OrderByFields = None, dir: OrderByDirection = OrderByDirection.asc):
        super().__init__(order_by, dir)