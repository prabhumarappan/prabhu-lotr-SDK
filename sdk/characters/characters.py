from sdk.quotes import Quote


class Character:
    def __init__(
        self, _id, height, race, gender, birth, spouse, death, realm, hair, name, wiki
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
        self.wiki: str = wiki

    def list_quotes(self) -> list[Quote]:
        return []


class Characters:
    def list(self) -> list[Character]:
        return []

    def get_character(self, _id) -> Character:
        return
