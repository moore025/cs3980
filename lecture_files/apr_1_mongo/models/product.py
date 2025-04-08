from beanie import Document


class Product(Document):
    name: str
    description: str
