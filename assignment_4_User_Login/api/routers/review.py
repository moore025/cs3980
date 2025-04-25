from typing import Annotated
from fastapi import APIRouter, Path, HTTPException, status

from models.review import Review, ReviewRequest

review_router = APIRouter()

max_id: int = (
    0  # NOT IDEAL because if you stop session and reload, then you open the door for duplicate ID's. Try doing a query of the database instead to get id numbers.
)


@review_router.post("", status_code=status.HTTP_201_CREATED)
async def add_review(review: ReviewRequest) -> Review:
    global max_id
    max_id += 1  # auto increment ID

    newReview = Review(
        id=max_id,
        title=review.restaurant,
        rating=review.rating,
        description=review.description,
    )
    await Review.insert_one(newReview)
    return newReview


@review_router.get("")
async def get_reviews() -> list[Review]:
    return await Review.find_all().to_list()


@review_router.get("/{id}")
async def get_review_by_id(id: int = Path(..., title="default")) -> Review:
    review = await Review.get(id)
    if review:
        return review
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"The review with ID={id} is not found.",
    )


@review_router.put("/{id}")
async def update_review(review: ReviewRequest, id: int) -> dict:
    existing_review = await Review.get(id)
    if existing_review:
        existing_review.restaurant = review.restaurant
        existing_review.rating = review.rating
        existing_review.description = review.description
        await existing_review.save()
        return {"message": "Review updated successfully"}

    return {"message": f"The review with ID={id} is not found."}


@review_router.delete("/{id}")
async def delete_review(id: int) -> dict:
    review = await Review.get(id)
    await review.delete()
    return {"message": f"The review with ID={id} has been deleted."}
