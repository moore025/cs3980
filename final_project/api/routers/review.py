from typing import Annotated
from beanie import PydanticObjectId
from fastapi import APIRouter, Path, HTTPException, status

from models.review import Review, ReviewRequest

review_router = APIRouter()


@review_router.post("", status_code=status.HTTP_201_CREATED)
async def add_review(review: ReviewRequest) -> Review:

    newReview = Review(
        restaurant=review.restaurant,
        rating=review.rating,
        description=review.description,
    )
    await Review.insert_one(newReview)
    return newReview


@review_router.get("")
async def get_reviews() -> list[Review]:
    return await Review.find_all().to_list()


@review_router.get("/{id}")
async def get_review_by_id(id: PydanticObjectId) -> Review:
    review = await Review.get(id)
    if review:
        return review
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"The review with ID={id} is not found.",
    )


@review_router.put("/{id}")
async def update_review(review: ReviewRequest, id: PydanticObjectId) -> dict:
    existing_review = await Review.get(id)
    if existing_review:
        existing_review.restaurant = review.restaurant
        existing_review.rating = review.rating
        existing_review.description = review.description
        await existing_review.save()
        return {"message": "Review updated successfully"}

    return {"message": f"The review with ID={id} is not found."}


@review_router.delete("/{id}")
async def delete_review(id: PydanticObjectId) -> dict:
    review = await Review.get(id)
    if review:
        await review.delete()
        return {"message": f"The review with ID={id} has been deleted."}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"The review with ID={id} is not found.",
    )
