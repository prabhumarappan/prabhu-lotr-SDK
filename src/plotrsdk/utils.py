import os
from termcolor import colored


class PaginatedResource:
    items: list
    total: int
    limit: int
    offset: int
    page: int
    pages: int

    def __init__(self, items, total, limit, offset, page, pages) -> None:
        self.items = items
        self.total = total
        self.limit = limit
        self.offset = offset
        self.page = page
        self.pages = pages


def get_token():
    token = os.getenv("LOTR_TOKEN")
    if token is None:
        print_error("LOTR_TOKEN is not set")
        raise Exception("LOTR_TOKEN is not set")
    return token


def build_url_params(pagination={}, sorting={}, filtering={}):
    params = {}
    params["limit"] = pagination["limit"] if "limit" in pagination else 10
    params["page"] = pagination["page"] if "page" in pagination else 0
    params["offset"] = pagination["offset"] if "offset" in pagination else 0
    if sorting:
        # last sorting key will be used to sort, others will be overwritten
        for key, value in sorting.items():
            params["sort"] = f"{key}:{value}"
    if filtering:
        for key, value in filtering.items():
            params[key] = value

    return params


def print_error(message):
    print(colored(message, "red"))


def print_warn(message):
    print(colored(message, "yellow"))
