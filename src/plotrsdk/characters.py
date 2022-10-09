from .quotes import Quote
from .service import LOTR
from .utils import build_url_params, print_error, PaginatedResource


class Character:
    token_required = True

    def __init__(
        self,
        _id,
        height,
        race,
        gender,
        birth,
        spouse,
        death,
        realm,
        hair,
        name,
        wiki_url,
    ):
        self._id: str = _id
        self.height: str = height
        self.race: str = race
        self.gender: str = gender
        self.birth: str = birth
        self.spouse: str = spouse
        self.death: str = death
        self.realm: str = realm
        self.hair: str = hair
        self.name: str = name
        self.wiki_url: str = wiki_url

    def list_quotes(self) -> list[Quote]:
        quotes = LOTR().make_request(
            method="GET",
            resource="character/{}/quote".format(self._id),
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


class Characters:
    token_required = True
    params = {}

    def get_characters(self):
        resource = "character"
        characters = LOTR().make_request(
            method="GET",
            resource=resource,
            params=self.params,
            headers={},
            attach_token=self.token_required,
        )

        result = [
            Character(
                c["_id"],
                c["height"],
                c["race"],
                c["gender"],
                c["birth"],
                c["spouse"],
                c["death"],
                c["realm"],
                c["hair"],
                c["name"],
                c["wikiUrl"],
            )
            for c in characters["docs"]
        ]

        return PaginatedResource(
            result,
            characters["total"],
            characters["limit"],
            characters["offset"],
            characters["page"] if "page" in characters else 0,
            characters["pages"] if "pages" in characters else 0,
        )

    def list(self, pagination={}, sorting={}, filtering={}):
        self.params = build_url_params(pagination, sorting, filtering)
        return self.get_characters()

    def next_page(self):
        if "page" not in self.params:
            print_error("No list params specified, please use list() first")
            return
        self.params["offset"] = (
            self.params["page"] * self.params["limit"] + self.params["limit"]
        )
        self.params["page"] += 1
        return self.get_characters()

    def get_page(self, page):
        if "page" not in self.params:
            print_error("No list params specified, please use list() first")
            return
        if page < 1:
            print_error("Page number cannot less than 1. Use list() to do this")
            return
        self.params["page"] = page
        self.params["offset"] = (page - 1) * self.params["limit"]
        return self.get_characters()

    def get_character(self, _id) -> Character:
        resource = "character/{}".format(_id)
        character = LOTR().make_request("GET", resource, {}, {}, self.token_required)

        if not character:
            return None
        character = character["docs"]
        if not character:
            return None
        character = character[0]

        return Character(
            character["_id"],
            character["height"],
            character["race"],
            character["gender"],
            character["birth"],
            character["spouse"],
            character["death"],
            character["realm"],
            character["hair"],
            character["name"],
            character["wikiUrl"],
        )
