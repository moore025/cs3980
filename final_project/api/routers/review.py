import logging
import base64
from typing import Annotated
from beanie import PydanticObjectId
from fastapi import (
    APIRouter,
    Depends,
    File,
    Form,
    Path,
    HTTPException,
    UploadFile,
    status,
)

from auth.jwt_auth import TokenData
from models.review import Review, ReviewRequest
from routers.user import get_user

review_router = APIRouter()
logger = logging.getLogger(__name__)


@review_router.post("", status_code=status.HTTP_201_CREATED)
async def add_review(
    # review: ReviewRequest,
    user: Annotated[TokenData, Depends(get_user)],
    restaurant: str = Form(...),
    rating: str = Form(...),
    description: str = Form(...),
    image: UploadFile = File(None),
) -> Review:
    logger.info(f"{user.username} is trying to add a review")
    base64_image = None
    if image:
        image_data = await image.read()
        base64_bytes = base64.b64encode(image_data)
        base64_image = (
            f"data:{image.content_type};base64,{base64_bytes.decode('utf-8')}"
        )
    newReview = Review(
        restaurant=restaurant,
        rating=rating,
        description=description,
        created_by=user.username,
        image=base64_image,
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
    id: PydanticObjectId,
    user: Annotated[TokenData, Depends(get_user)],
    restaurant: str = Form(...),
    rating: str = Form(...),
    description: str = Form(...),
    image: UploadFile = File(None),
) -> dict:
    existing_review = await Review.get(id)
    if existing_review:
        existing_review.restaurant = restaurant
        existing_review.rating = rating
        existing_review.description = description

        if image:
            image_data = await image.read()
            base64_bytes = base64.b64encode(image_data)
            base64_image = (
                f"data:{image.content_type};base64,{base64_bytes.decode('utf-8')}"
            )
            existing_review.image = base64_image

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
