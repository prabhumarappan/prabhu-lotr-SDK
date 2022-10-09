from .chapters import Chapter
from .service import LOTR
from .utils import build_url_params, print_error, PaginatedResource


class Book:
    token_required = False

    def __init__(self, _id, name):
        self._id: str = _id
        self.name: str = name

    def list_chapters(self):
        chapters = LOTR().make_request(
            method="GET",
            resource="book/{}/chapter".format(self._id),
            params={},
            headers={},
            attach_token=self.token_required,
        )

        result = [
            Chapter(chapter["_id"], chapter["chapterName"])
            for chapter in chapters["docs"]
        ]

        return PaginatedResource(
            result,
            chapters["total"],
            chapters["limit"],
            chapters["offset"],
            chapters["page"] if "page" in chapters else 0,
            chapters["pages"] if "pages" in chapters else 0,
        )

    def __repr__(self) -> str:
        return f"<Book: {self.name}>"


class Books:
    token_required = False
    params = {}

    def _get_books(self):
        resource = "book"
        books = LOTR().make_request(
            method="GET",
            resource=resource,
            params=self.params,
            headers={},
            attach_token=self.token_required,
        )

        result = [Book(book["_id"], book["name"]) for book in books["docs"]]

        return PaginatedResource(
            result,
            books["total"],
            books["limit"],
            books["offset"],
            books["page"] if "page" in books else 0,
            books["pages"] if "pages" in books else 0,
        )

    def list(self, pagination={}, sorting={}, filtering={}):
        self.params = build_url_params(pagination, sorting, filtering)
        return self._get_books()

    def next_page(self):
        if "page" not in self.params:
            print_error("No list params specified, please use list() first")
            return
        self.params["offset"] = (
            self.params["page"] * self.params["limit"] + self.params["limit"]
        )
        self.params["page"] += 1
        return self._get_books()

    def get_page(self, page):
        if "page" not in self.params:
            print_error("No list params specified, please use list() first")
            return
        if page < 1:
            print_error("Page number cannot less than 1. Use list() to do this")
            return
        self.params["page"] = page
        self.params["offset"] = (page - 1) * self.params["limit"]
        return self._get_books()

    def get_book(self, _id):
        resource = "book/{}".format(_id)
        book = LOTR().make_request("GET", resource, {}, {}, self.token_required)

        if not book:
            return None
        book = book["docs"]
        if not book:
            return None
        book = book[0]

        return Book(book["_id"], book["name"])
