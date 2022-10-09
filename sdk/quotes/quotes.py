class Quote:
    def __init__(self, _id, dialog, movie, character) -> None:
        self._id: str = _id
        self.dialog: str = dialog
        self.movie: str = movie
        self.character: str = character


class Quotes:
    def list(self) -> list[Quote]:
        return []

    def get_quote(self, _id) -> Quote:
        return []
