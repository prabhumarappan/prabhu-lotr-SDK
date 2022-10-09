from .quotes import Quote
from .service import LOTR
from .utils import build_url_params, print_error, PaginatedResource


class Movie:
    token_required = True

    def __init__(
        self,
        _id,
        name,
        runtime,
        budget,
        box_office,
        academy_nominations,
        academy_wins,
        rotten_tomatoes_score,
    ) -> None:
        self._id: str = _id
        self.name: str = name
        self.runtime: int = runtime
        self.budget: float = budget
        self.box_office: float = box_office
        self.academy_nominations: int = academy_nominations
        self.academy_wins: int = academy_wins
        self.rotten_tomatoes_score: int = rotten_tomatoes_score

    def list_quotes(self) -> list[Quote]:
        quotes = LOTR().make_request(
            method="GET",
            resource="movie/{}/quote".format(self._id),
            params={},
            headers={},
            attach_token=self.token_required,
        )

        result = [
            Quote(quote["_id"], quote["dialog"], quote["movie"], quote["character"])
            for quote in quotes["docs"]
        ]

        return PaginatedResource(
            result,
            quotes["total"],
            quotes["limit"],
            quotes["offset"],
            quotes["page"] if "page" in quotes else 0,
            quotes["pages"] if "pages" in quotes else 0,
        )

    def __repr__(self) -> str:
        return f"<Character: {self.name}>"


class Movies:
    token_required = True
    params = {}

    def get_movies(self):
        resource = "movie"
        movies = LOTR().make_request(
            method="GET",
            resource=resource,
            params=self.params,
            headers={},
            attach_token=self.token_required,
        )

        result = [
            Movie(
                m["_id"],
                m["name"],
                m["runtimeInMinutes"],
                m["budgetInMillions"],
                m["boxOfficeRevenueInMillions"],
                m["academyAwardNominations"],
                m["academyAwardWins"],
                m["rottenTomatoesScore"],
            )
            for m in movies["docs"]
        ]

        return PaginatedResource(
            result,
            movies["total"],
            movies["limit"],
            movies["offset"],
            movies["page"] if "page" in movies else 0,
            movies["pages"] if "pages" in movies else 0,
        )

    def list(self, pagination={}, sorting={}, filtering={}):
        self.params = build_url_params(pagination, sorting, filtering)
        return self.get_movies()

    def next_page(self):
        if "page" not in self.params:
            print_error("No list params specified, please use list() first")
            return
        self.params["offset"] = (
            self.params["page"] * self.params["limit"] + self.params["limit"]
        )
        self.params["page"] += 1
        return self.get_movies()

    def get_page(self, page):
        if "page" not in self.params:
            print_error("No list params specified, please use list() first")
            return
        if page < 1:
            print_error("Page number cannot less than 1. Use list() to do this")
            return
        self.params["page"] = page
        self.params["offset"] = (page - 1) * self.params["limit"]
        return self.get_movies()

    def get_movie(self, _id) -> Movie:
        resource = "movie/{}".format(_id)
        movie = LOTR().make_request("GET", resource, {}, {}, self.token_required)

        if not movie:
            return None
        movie = movie["docs"]
        if not movie:
            return None
        movie = movie[0]

        return Movie(
            movie["_id"],
            movie["name"],
            movie["runtimeInMinutes"],
            movie["budgetInMillions"],
            movie["boxOfficeRevenueInMillions"],
            movie["academyAwardNominations"],
            movie["academyAwardWins"],
            movie["rottenTomatoesScore"],
        )
