import logging
from typing import Annotated
from beanie import PydanticObjectId
from fastapi import APIRouter, Depends, Path, HTTPException, status

from auth.jwt_auth import TokenData
from models.review import Review, ReviewRequest
from routers.user import get_user

review_router = APIRouter()
logger = logging.getLogger(__name__)


@review_router.post("", status_code=status.HTTP_201_CREATED)
async def add_review(
    review: ReviewRequest, user: Annotated[TokenData, Depends(get_user)]
) -> Review:
    logger.info(f"{user.username} is trying to add a review")
    newReview = Review(
        restaurant=review.restaurant,
        rating=review.rating,
        description=review.description,
        created_by=user.username,
    )
    newReview = await Review.insert_one(newReview)
    logger.info(f"{user.username} added a new review")
    return newReview


@review_router.get("")
async def get_reviews(user: Annotated[TokenData, Depends(get_user)]) -> list[Review]:
    if not user or not user.username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Please login.",
        )
    if user.role != "AdminUser":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"You don't have enough permissions for this action.",
        )
    logger.info(f"{user.username} is retrieving all reviews")
    return await Review.find_all().to_list()


@review_router.get("/my")
async def get_my_reviews(user: Annotated[TokenData, Depends(get_user)]) -> list[Review]:
    if not user or not user.username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Please login.",
        )
    logger.info(f"{user.username} is retrieving their reviews")
    return await Review.find(Review.created_by == user.username).to_list()


@review_router.get("/search")
async def get_search_reviews(
    restaurant: str, user: Annotated[TokenData, Depends(get_user)]
) -> list[Review]:
    if not user or not user.username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Please login.",
        )
    logger.info(f"{user.username} is searching for reviews")
    return await Review.find(Review.restaurant == restaurant).to_list()


@review_router.put("/{id}")
async def update_review(
    review: ReviewRequest,
    id: PydanticObjectId,
    user: Annotated[TokenData, Depends(get_user)],
) -> dict:
    existing_review = await Review.get(id)
    if existing_review:
        existing_review.restaurant = review.restaurant
        existing_review.rating = review.rating
        existing_review.description = review.description
        await existing_review.save()
        logger.info({f"{user.username} edited a review"})
        return {"message": "Review updated successfully"}

    return {"message": f"The review with ID={id} is not found."}


@review_router.delete("/{id}")
async def delete_review(
    id: PydanticObjectId, user: Annotated[TokenData, Depends(get_user)]
) -> dict:
    review = await Review.get(id)
    if review:
        logger.info(f"{user.username} is deleting review with ID={id}")
        await review.delete()
        return {"message": f"The review with ID={id} has been deleted."}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"The review with ID={id} is not found.",
    )
