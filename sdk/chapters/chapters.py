class Chapter:
    def __init__(self, _id, chapter_name) -> None:
        _id: str = _id
        chapter_name: str = chapter_name


class Chapters:
    def list(self) -> list[Chapter]:
        return []

    def get_chapter(self, _id) -> Chapter:
        return
