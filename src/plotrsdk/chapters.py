from .service import LOTR
from .utils import build_url_params, print_error, PaginatedResource


class Chapter:
    token_required = True

    def __init__(self, _id, chapter_name) -> None:
        self._id: str = _id
        self.chapter_name: str = chapter_name

    def __repr__(self) -> str:
        return f"<Chapter: {self.chapter_name}>"


class Chapters:
    token_required = True
    params = {}

    def get_chapters(self):
        resource = "chapter"
        chapters = LOTR().make_request(
            method="GET",
            resource=resource,
            params=self.params,
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

    def list(self, pagination={}, sorting={}, filtering={}):
        self.params = build_url_params(pagination, sorting, filtering)
        return self.get_chapters()

    def next_page(self):
        if "page" not in self.params:
            print_error("No list params specified, please use list() first")
            return
        self.params["offset"] = (
            self.params["page"] * self.params["limit"] + self.params["limit"]
        )
        self.params["page"] += 1
        return self.get_chapters()

    def get_page(self, page):
        if "page" not in self.params:
            print_error("No list params specified, please use list() first")
            return
        if page < 1:
            print_error("Page number cannot less than 1. Use list() to do this")
            return
        self.params["page"] = page
        self.params["offset"] = (page - 1) * self.params["limit"]
        return self.get_chapters()

    def get_chapter(self, _id) -> Chapter:
        resource = "chapter/{}".format(_id)
        chapter = LOTR().make_request("GET", resource, {}, {}, self.token_required)

        if not chapter:
            return None
        chapter = chapter["docs"]
        if not chapter:
            return None
        chapter = chapter[0]

        return Chapter(chapter["_id"], chapter["chapterName"])
