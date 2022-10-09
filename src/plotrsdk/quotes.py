from .service import LOTR
from .utils import build_url_params, print_error, PaginatedResource


class Quote:
    token_required = True

    def __init__(self, _id, dialog, movie, character) -> None:
        self._id: str = _id
        self.dialog: str = dialog
        self.movie: str = movie
        self.character: str = character

    def __repr__(self) -> str:
        return f"<Dialog: {self.dialog}>"


class Quotes:
    token_required = True
    params = {}

    def _get_quotes(self):
        resource = "quote"
        quotes = LOTR().make_request(
            method="GET",
            resource=resource,
            params=self.params,
            headers={},
            attach_token=self.token_required,
        )

        result = [
            Quote(q["_id"], q["dialog"], q["movie"], q["character"])
            for q in quotes["docs"]
        ]

        return PaginatedResource(
            result,
            quotes["total"],
            quotes["limit"],
            quotes["offset"],
            quotes["page"] if "page" in quotes else 0,
            quotes["pages"] if "pages" in quotes else 0,
        )

    def list(self, pagination={}, sorting={}, filtering={}):
        self.params = build_url_params(pagination, sorting, filtering)
        return self._get_quotes()

    def next_page(self):
        if "page" not in self.params:
            print_error("No list params specified, please use list() first")
            return
        self.params["offset"] = (
            self.params["page"] * self.params["limit"] + self.params["limit"]
        )
        self.params["page"] += 1
        return self._get_quotes()

    def get_page(self, page):
        if "page" not in self.params:
            print_error("No list params specified, please use list() first")
            return
        if page < 1:
            print_error("Page number cannot less than 1. Use list() to do this")
            return
        self.params["page"] = page
        self.params["offset"] = (page - 1) * self.params["limit"]
        return self._get_quotes()

    def get_quote(self, _id) -> Quote:
        resource = "quote/{}".format(_id)
        quote = LOTR().make_request("GET", resource, {}, {}, self.token_required)

        if not quote:
            return None
        quote = quote["docs"]
        if not quote:
            return None
        quote = quote[0]

        return Quote(quote["_id"], quote["dialog"], quote["movie"], quote["character"])
