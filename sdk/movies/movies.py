from sdk.quotes import Quote


class Movie:
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
        return []


class Movies:
    def list(self) -> list[Movie]:
        return []
