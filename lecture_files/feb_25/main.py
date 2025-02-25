from typing import Annotated
from fastapi import FastAPI, Path

# Use /docs for better viewing or alternatively /redoc

app = FastAPI(title="Nick's API", summary="This is my API from Feb 25")


@app.get(
    "/items/{item_id}",
    summary="Create an item",
    description="Create an item with all the information, name, description, price, tax, and set of unique tags",
)
async def get_item_by_id(
    item_id: Annotated[
        int,
        Path(
            title="This is the item ID, which should be an integer.",
            ge=0,
            le=1000,
            # multiple_of=2,
        ),
    ]
) -> dict:
    return {"item_id": item_id}  # Basic API endpoint learned from previous lectures
