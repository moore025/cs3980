from fastapi import APIRouter, Path, HTTPException, status
from model import Review, ReviewRequest
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

review_router = APIRouter()

review_list = []
max_id: int = 0


@review_router.post("", status_code=status.HTTP_201_CREATED)
async def add_review(review: ReviewRequest) -> Review:
    global max_id
    max_id += 1  # auto increment ID

    newReview = Review(
        id=max_id,
        restaurant=review.restaurant,
        rating=review.rating,
        description=review.description,
    )
    review_list.append(newReview)
    return newReview


@review_router.get("")
async def get_reviews() -> list[Review]:
    return review_list


@review_router.get("/{id}")
async def get_review_by_id(id: int = Path(..., restaurant="default")) -> Review:
    for review in review_list:
        if review.id == id:
            return review

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"The review with ID={id} is not found.",
    )


@review_router.put("/{id}")
async def update_review(review: ReviewRequest, id: int) -> dict:
    for x in review_list:
        if x.id == id:
            x.restaurant = review.restaurant
            x.rating = review.rating
            x.description = review.description
            return {"message": "Review updated successfully"}

    return {"message": f"The review with ID={id} is not found."}


@review_router.delete("/{id}")
async def delete_review(id: int) -> dict:
    for i in range(len(review_list)):
        review = review_list[i]
        if review.id == id:
            review_list.pop(i)
            return {"message": f"The review with ID={id} has been deleted."}

    return {"message": f"The review with ID={id} is not found."}
