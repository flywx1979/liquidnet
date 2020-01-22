from mypy_extensions import TypedDict


class BookRequestContract(TypedDict, total=False):
    title: str
    email: str
