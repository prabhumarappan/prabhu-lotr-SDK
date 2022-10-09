from sdk.chapters import Chapter


class Book:
    def __init__(self, _id, name):
        _id: str = _id
        name: str = name

    def chapters() -> list[Chapter]:
        return []


class Books:
    def list(self) -> list[Book]:
        return []

    def get_book(self, _id) -> Book:
        return
